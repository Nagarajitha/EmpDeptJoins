from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models import Q


def innerEquijoins(request):
    #Joined Data Of Emp and Dept
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


def selfjoins(request):

    #EMJD -->Employee Manager Joining Data (table1 EMP , Table2 MGR)
    EMJD = Emp.objects.select_related('MGR').all()

    #emp comm is null
    EMJD = Emp.objects.select_related('MGR').filter(COMM__isnull =True)

    #emp comm is not null
    EMJD = Emp.objects.select_related('MGR').filter(COMM__isnull =False)

    #emp whose mgr name contains'a' in it
    EMJD = Emp.objects.select_related('MGR').filter(MGR__ENAME__contains ='a')

    # emp data whose mgr doesnt have any manager
    EMJD = Emp.objects.select_related('MGR').filter(MGR__isnull =True)

    #emp whose manager name starts with 'b' or 'c'
    EMJD = Emp.objects.select_related('MGR').filter(Q(MGR__ENAME__startswith ='b' )|Q(MGR__ENAME__startswith ='c' )) 

    #emp whose name contains 's' and mgr name contains 'a' or 'b'
    EMJD = Emp.objects.select_related('MGR').filter(Q(ENAME__contains ='s') & Q(MGR__ENAME__contains ='a')|Q(MGR__ENAME__contains ='b'))

    #emp hiredate before 1985
    EMJD = Emp.objects.select_related('MGR').filter(HIREDATE__year__lt = 1985)

    #emp hiredate after 1985 and before 1990
    EMJD = Emp.objects.select_related('MGR').filter(HIREDATE__year__gt = 1985 ,HIREDATE__year__lt = 1990)

    #emp whose mgr sal is 5000
    EMJD = Emp.objects.select_related('MGR').filter(MGR__SAL=5000)

    #emp whose mgr sal is in range 3000 - 5000
    EMJD = Emp.objects.select_related('MGR').filter(MGR__SAL__range =(3000,5000))

    #emp hiredate in month of dec
    EMJD = Emp.objects.select_related('MGR').filter(HIREDATE__month = 12)
    
    #EMJD = Emp.objects.select_related('MGR').all()
    

    d={'EMJD':EMJD}
    return render(request,'selfjoins.html',d)
