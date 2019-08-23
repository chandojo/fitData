from django.db import models

class Muscle(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class MuscleGroup(models.Model):
    name = models.CharField(max_length=255)
    muscle_1 = models.ForeignKey('Muscle', on_delete=models.PROTECT, related_name='muscle_1')
    muscle_2 = models.ForeignKey('Muscle', on_delete=models.PROTECT, related_name='muscle_2', null=True, blank=True)
    muscle_3 = models.ForeignKey('Muscle', on_delete=models.PROTECT, related_name='muscle_3', null=True, blank=True)
    muscle_4 = models.ForeignKey('Muscle', on_delete=models.PROTECT, related_name='muscle_4', null=True, blank=True)
    muscle_5 = models.ForeignKey('Muscle', on_delete=models.PROTECT, related_name='muscle_5', null=True, blank=True)
    muscle_6 = models.ForeignKey('Muscle', on_delete=models.PROTECT, related_name='muscle_6', null=True, blank=True)
    muscle_7 = models.ForeignKey('Muscle', on_delete=models.PROTECT, related_name='muscle_7', null=True, blank=True)
    muscle_8 = models.ForeignKey('Muscle', on_delete=models.PROTECT, related_name='muscle_8', null=True, blank=True)
    muscle_9 = models.ForeignKey('Muscle', on_delete=models.PROTECT, related_name='muscle_9', null=True, blank=True)
    muscle_10 = models.ForeignKey('Muscle', on_delete=models.PROTECT, related_name='muscle_10', null=True, blank=True)

    def __str__(self):
        return self.name

class ExerciseDifficulty(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Movement(models.Model):
    name = models.CharField(max_length=255)
    movement_plane = models.ForeignKey('MovementPlane', on_delete=models.PROTECT)
    agonist_muscle_group = models.ForeignKey('MuscleGroup', on_delete=models.PROTECT, related_name='agonist_muscle_group',null=True, blank=True)
    agonist = models.ForeignKey('Muscle', on_delete=models.PROTECT, related_name='agonist_muscle', null=True, blank=True)
    synergist = models.ForeignKey('Muscle', on_delete=models.PROTECT, related_name='synergist_muscle', null=True, blank=True)
    antagonist = models.ForeignKey('Muscle', on_delete=models.PROTECT, related_name='antagonist_muscle', null=True, blank=True)
    joint_1 = models.ForeignKey('Joint', on_delete=models.PROTECT, related_name='joint_1', null=True, blank=True)
    joint_2 = models.ForeignKey('Joint', on_delete=models.PROTECT, related_name='joint_2', null=True, blank=True)

    def __str__(self):
        return self.name

class MovementPlane(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Joint(models.Model):
    name = models.CharField(max_length=255)
    joint_type = models.ForeignKey('JointType', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class JointType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ContractionType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class JointNumber(models.Model):
    number = models.IntegerField()

    def __str__(self):
        return str(self.number)

class Sides(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=255)
    joint_number = models.ForeignKey('JointNumber', on_delete=models.PROTECT)
    sides = models.ForeignKey('Sides', on_delete=models.PROTECT)
    movement_1 = models.ForeignKey('Movement', on_delete=models.PROTECT, related_name='movement_1')
    movement_2 = models.ForeignKey('Movement', on_delete=models.PROTECT, related_name='movement_2', null=True, blank=True)
    movement_3 = models.ForeignKey('Movement', on_delete=models.PROTECT, related_name='movement_3',null=True, blank=True)
    equipment = models.ForeignKey('Equipment', on_delete=models.PROTECT)
    cues = models.TextField()
    video = models.URLField(max_length=200)
    difficulty = models.ForeignKey('ExerciseDifficulty', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name

class WorkoutExercises(models.Model):
    exercise = models.ForeignKey('Exercise', on_delete=models.PROTECT)
    sets = models.IntegerField()
    reps = models.FloatField()
    rep_duration = models.BooleanField(default=False)
    rest_btwn_sets_sec = models.FloatField()
    contraction_type = models.ForeignKey('ContractionType', on_delete=models.PROTECT)
    intensity = models.FloatField()
    intensity_percentage = models.BooleanField(default=False)
    workout_plan = models.ForeignKey('Workout', on_delete=models.PROTECT)

    def __str__(self):
        return '{workout} - {exercise}'.format(workout=self.workout_plan, exercise=self.exercise)

class WorkoutType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class WorkoutDuration(models.Model):
    weeks = models.FloatField()

    def __str__(self):
        return str(self.weeks)

class WorkoutFrequency(models.Model):
    days_per_week = models.IntegerField()

    def __str__(self):
        return str(self.days_per_week)

class WorkoutPhase(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class SeasonPlanDuration(models.Model):
    season_duration = models.FloatField()

    def __str__(self):
        return self.season_duration

class Activity(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class SeasonPlan(models.Model):
    name = models.CharField(max_length=255)
    activity = models.ForeignKey('Activity', on_delete=models.PROTECT)
    season_duration = models.ForeignKey('SeasonPlanDuration', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class WorkoutDifficulty(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Workout(models.Model):
    name = models.CharField(max_length=255)
    workout_type = models.ForeignKey('WorkoutType', on_delete=models.PROTECT)
    workout_duration = models.ForeignKey('WorkoutDuration', on_delete=models.PROTECT)
    workout_frequency = models.ForeignKey('WorkoutFrequency', on_delete=models.PROTECT)
    workout_phase = models.ForeignKey('WorkoutPhase', on_delete=models.PROTECT)
    season_plan = models.ForeignKey('SeasonPlan', on_delete=models.PROTECT, null=True, blank=True)
    workout_difficulty = models.ForeignKey('WorkoutDifficulty', on_delete=models.PROTECT)

    def __str__(self):
        return self.name
