from django.db import models
from .member import Member
from .employee import Employee
from .book import Book
from datetime import timedelta


class LendBook(models.Model):
    lend_date = models.DateField()
    return_date = models.DateField()
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.return_date = self.lend_date + timedelta(days=2)
        super(LendBook, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee} prestó el libro: [{self.book}] a {self.member} el {self.lend_date}"
