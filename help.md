´´´
def save(self, *args, **kwargs):
        try:
            self.exam_taken
        except:
            self.exam_taken = Exam.objects.first()
        super().save(*args, **kwargs)
´´´