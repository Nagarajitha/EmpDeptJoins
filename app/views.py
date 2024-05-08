from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models import Q


def innerEquijoins(request):
    JDED = Emp.objects.select_related('DEPTNO').all()

    JDED = Emp.objects.select_related('DEPTNO').filter(DEPTNO = 30)

    JDED = Emp.objects.select_related('DEPTNO').filter(DEPTNO = 10)

    JDED = Emp.objects.select_related('DEPTNO').filter(EMPNO = 7788)

    JDED = Emp.objects.select_related('DEPTNO').filter(DEPTNO = 30)

    JDED = Emp.objects.select_related('DEPTNO').filter(ENAME__contains ='s')

    JDED = Emp.objects.select_related('DEPTNO').filter(JOB__endswith = 't')

    JDED = Emp.objects.select_related('DEPTNO').filter(ENAME__contains ='e' , SAL__gt = 500)

    JDED = Emp.objects.select_related('DEPTNO').filter(Q(ENAME__contains ='e') | Q(SAL__gt = 500) & Q(COMM__gt = 10))

    JDED = Emp.objects.select_related('DEPTNO').filter(Q(SAL__gt = 500) & Q(COMM__gt = 10))

    #when we want to fetch data with condition in parent table(dept)-> we have use  (commonCol__ColNAme = value) ********
    
    JDED = Emp.objects.select_related('DEPTNO').filter(Q(SAL__gt = 500) & Q(COMM__gt = 10) | Q(DEPTNO__DNAME ='NEW YORK'))

    JDED = Emp.objects.select_related('DEPTNO').filter(Q(SAL__lt = 500) & Q(COMM__gt = 10))

    JDED = Emp.objects.select_related('DEPTNO').filter(SAL__range =[100,2000])

    JDED = Emp.objects.select_related('DEPTNO').filter(Q(SAL__gt = 500) & Q(HIREDATE__lt = '1999-09-09'))

    JDED = Emp.objects.select_related('DEPTNO').filter(JOB='MANAGER')

    JDED = Emp.objects.select_related('DEPTNO').filter(MGR=7566)

    JDED = Emp.objects.select_related('DEPTNO').filter(DEPTNO__LOC ='DALLAS')

    JDED = Emp.objects.select_related('DEPTNO').filter(DEPTNO__DNAME__in =('ACCOUNTING','SALES'))

    JDED = Emp.objects.select_related('DEPTNO').filter(DEPTNO__DNAME__in =('ACCOUNTING','SALES'), DEPTNO =10 , JOB ='MANAGER')


    d={'JDED':JDED}
    return render(request,'innerEquijoins.html',d)