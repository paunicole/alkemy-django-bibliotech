from django.db import models
from .member import Member
from .employee import Employee
from .book import Book


class LendBook(models.Model):
    lend_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(auto_now=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.employee} prestó el libro: [{self.book}] a {self.member} el {self.lend_date}"
