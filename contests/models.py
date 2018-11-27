from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from practice.models import Track,Question,Record
import operator
from django.utils import timezone
from userprofile.models import Profile


class Contest(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    image = models.CharField(blank=True,null=True,max_length=1000)

    def get_duration(self):
        return self.end_date - self.start_date

    def status(self,user):
        """

         :return:  1 --> Contest is live
         :return: -1 --> Contest has finished
         :return:  0 --> Contest has not started
        """
        if  timezone.now()<self.start_date:
            return 0
          
        elif self.start_date<=timezone.now()< self.end_date:
            return 1
        else:
            self.end_contest(user)
            return -1
    def get_start_date(self):
        return str(self.start_date)

    def start_contest(self):
        """

        :return: leaderboard
        """
        leaderboard = Leaderboard.objects.get_or_create(contest=self)
        return leaderboard

    def end_contest(self,user):
        # Addig all the contest's questions to practice questions
        # and then deleting this data
        questions = ContestQuestion.objects.all().filter(contest=self)
        leaderboard = Leaderboard.objects.get(contest=self)
        leaderboard.set_leaderboard()
        leaderboard.set_points()

        ques = []
        for question in questions:
            q = Question.objects.create(

            track=question.track,
            title = question.title,
            description = question.description,
            testcases = question.testcases,
            testcases_output = question.testcases_output,
            explanation = question.explanation,
            inputs = question.inputs,
            output = question.output,
            points = question.points,
            right_count = question.right_count,
            wrong_count = question.wrong_count,

            )
            ques.append(q)
        for q in ques:
            Record.objects.create(user=user,question=q)
        questions.delete()

    def get_end_date(self):
        return str(self.end_date)

    def __str__(self):
        return self.title


class ContestQuestion(models.Model):
    contest = models.ForeignKey(Contest,on_delete=models.CASCADE,related_name='ContestQuestionContest')
    track = models.ForeignKey(Track,on_delete=models.CASCADE,related_name='ContestQuestionTrack')
    title = models.CharField(max_length=400)
    description = models.TextField(max_length=1000,null=True)
    testcases = models.TextField(max_length=100)
    testcases_output = models.TextField(max_length=100,blank=True)
    explanation = models.TextField(max_length=1000,blank=True)
    inputs = models.TextField(max_length=50000)
    output = models.TextField(max_length=10000)
    points = models.PositiveIntegerField(default=settings.DEFAULT_POINTS)
    right_count = models.PositiveIntegerField(default=0)
    wrong_count = models.PositiveIntegerField(default=0)


    def total_submission(self):
        return self.wrong_count+self.right_count

    def get_percentage_correct(self):
        try:
            return "%.2f" %((self.right_count*100)/(self.wrong_count+self.right_count))
        except ZeroDivisionError:
            return 0
    def get_percentage_wrong(self):
        return 100-self.get_percentage_correct()

    def test(self,output,user):
        for i in range(100): print(ContestRecord.objects.all())

        if output.lstrip().rstrip()==self.output.lstrip().rstrip().replace("\r",""):
            if len(ContestRecord.objects.all().filter(contest=self.contest,user=user,question=self))!=0:
                pass
                for i in range(10):print("already exists")
            else:
                self.right_count += 1
                self.save()
                ContestRecord.objects.create(user = user,question=self,contest=self.contest)
                user.profile.add_points(self.points)
            return True
        else:
            self.wrong_count+=1
            self.save()
            return False

    def __str__(self):
        return self.title

class ContestRecord(models.Model):
    contest  = models.ForeignKey(Contest,on_delete=models.CASCADE,related_name='ContestRecordContest')
    user     = models.ForeignKey(User,on_delete=models.CASCADE,related_name="ContestRecordUser")
    question = models.ForeignKey(ContestQuestion,on_delete=models.CASCADE,related_name="ContestRecordQuestion")

    def __str__(self):
        return str(self.contest)+" -- "+str(self.question)+" -- "+str(self.user)

class Leaderboard(models.Model):
    contest = models.ForeignKey(Contest,on_delete=models.CASCADE)
    leaderboard = models.CharField(max_length=1000,default="[]")
    total_points = models.PositiveIntegerField(default = 0)

    def get_leaderboard(self):
        if self.total_points == 0:
            self.set_points()
        if self.leaderboard == "[]":
            try:
                records = ContestRecord.objects.all().filter(contest = self.contest)
            except:
                records=[]
            l = {}
            for r in records:
                try:
                    l[r.user.profile] += r.question.points
                except:
                    l[r.user.profile] = r.question.points
                    l[r.user.profile] = r.question.points
            leaderboard = sorted(l.items(), key=operator.itemgetter(1))
            leaderboard.reverse()
        else:
            leaderboard=[]
            l = eval(self.leaderboard)
            for profile_id,points in l:
                leaderboard.append((Profile.objects.get(id=profile_id),points))
        return leaderboard

    def set_leaderboard(self):
        if self.leaderboard=="[]":
            records = ContestRecord.objects.all().filter(contest=self.contest)
            l = {}
            for r in records:
                try:
                    l[r.user.profile.id] += r.question.points
                except:
                    l[r.user.profile.id] = r.question.points
                    l[r.user.profile.id] = r.question.points
            leaderboard = sorted(l.items(), key=operator.itemgetter(1))
            leaderboard.reverse()
            self.leaderboard = str(leaderboard)
            self.save()
        return self.leaderboard

    def set_points(self):
        questions = ContestQuestion.objects.filter(contest = self.contest)
        p=0
        for question in questions:
            p += question.points
        self.total_points += p
        self.save()

    def __str__(self):
        return str(self.contest)+"-- Leaderboard"