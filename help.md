´´´
def save(self, *args, **kwargs):
        try:
            self.exam_taken
        except:
            self.exam_taken = Exam.objects.first()
        super().save(*args, **kwargs)
´´´

´´´
parent_id = models.ForeignKey('self',  
    on_delete=models.PROTECT,
    verbose_name=('Parent'),
    null=True,
    blank=True,
    related_name='children')
    ´´´