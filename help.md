# Save
´´´
def save(self, *args, **kwargs):
        try:
            self.exam_taken
        except:
            self.exam_taken = Exam.objects.first()
        super().save(*args, **kwargs)
´´´

# Many2One Self
´´´
parent_id = models.ForeignKey('self',  
    on_delete=models.PROTECT,
    verbose_name=('Parent'),
    null=True,
    blank=True,
    related_name='children')
´´´

# Many2One 
´´´
partner_id = models.ForeignKey(
        Contact,
        related_name='sale_order_partner',
        on_delete=models.PROTECT,
        verbose_name='Partner',
        null=True,
        blank=True
    )
´´´