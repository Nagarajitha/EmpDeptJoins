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

def empMgrDept(request):
    #Employee Manager Department Joining Data

    #need to write common columns of tables 
    EMDJD = Emp.objects.select_related('DEPTNO','MGR').all()

    EMDJD =EMDJD = Emp.objects.select_related('DEPTNO','MGR').filter(MGR__DEPTNO =20)

    EMDJD = Emp.objects.select_related('DEPTNO','MGR').filter(JOB ='MANAGER')

    EMDJD = Emp.objects.select_related('DEPTNO','MGR').filter(MGR__SAL__gt = 2000,MGR__SAL__lt = 3000)

    EMDJD = Emp.objects.select_related('DEPTNO','MGR').filter(HIREDATE__year__lt = 1985)

    EMDJD = Emp.objects.select_related('DEPTNO','MGR').filter(MGR__ENAME ='SCOTT')

    EMDJD = Emp.objects.select_related('DEPTNO','MGR').filter(MGR__COMM__isnull = True , MGR__SAL__gt = 4000)

    EMDJD = Emp.objects.select_related('DEPTNO','MGR').filter(DEPTNO__in = (20,30,40))

    EMDJD = Emp.objects.select_related('DEPTNO','MGR').filter(MGR__DEPTNO__in = (20,30,40))

    EMDJD = Emp.objects.select_related('DEPTNO','MGR').filter(MGR__DEPTNO__in = (20,40))

    EMDJD = Emp.objects.select_related('DEPTNO','MGR').filter(DEPTNO__in = (20,30,40) , MGR__DEPTNO__in=(20,30,40))

    EMDJD = Emp.objects.select_related('DEPTNO','MGR').filter(DEPTNO__in = (20,30,40) , JOB ='SALESMAN')

    EMDJD = Emp.objects.select_related('DEPTNO','MGR').filter(Q(JOB ='SALESMAN') |Q(MGR__JOB__in = ('SALESMAN','MANAGER','ANALYST')))

    EMDJD = Emp.objects.select_related('DEPTNO','MGR').filter(MGR__ENAME ='KING')

    EMDJD = Emp.objects.select_related('DEPTNO','MGR').exclude(MGR__ENAME ='KING')

    EMDJD = Emp.objects.select_related('DEPTNO','MGR').exclude(MGR__ENAME ='BLAKE')



    #Dealing with Raw SQL Quries -- > we use extra(where = [' condition(col_name)'])

    #get all Enames having exactly 5 charaters in it
    EMDJD = Emp.objects.extra(where = [" LENGTH(ENAME) = 5"])

    EMDJD = Emp.objects.extra(where = [" ENAME LIKE '%_n'"])

    EMDJD = Emp.objects.extra(where = [" LENGTH(JOB) =  5"])

    EMDJD = Emp.objects.extra(where = [" ENAME LIKE 'A%'"])

    EMDJD = Emp.objects.extra(where = [" COMM > 200"])

    EMDJD = Emp.objects.extra(where = [" (HIREDATE > '1980-01-01') AND (HIREDATE < '1990-01-01')"])

    EMDJD = Emp.objects.extra(where = [" (HIREDATE > '1980-01-01') AND (HIREDATE < '1985-01-01')"])

    #As DEPTNO is FK column we need to use select_related('DEPTNO','MGR') inorder to get the data
    EMDJD = Emp.objects.select_related('DEPTNO','MGR').extra(where = ["DEPTNO = 10 "])

    EMDJD = Emp.objects.select_related('DEPTNO','MGR').extra(where = ["DEPTNO in (10,20) "])

    EMDJD = Emp.objects.select_related('DEPTNO','MGR').extra(where = ["DEPTNO in (10,20) "])

    

    #EMDJD = Emp.objects.select_related('DEPTNO','MGR').all()

    d={'EMDJD':EMDJD}

    return render(request,'empMgrDept.html',d)


def empSalgrade(request):

    #Emp Dept Salgrade Join Data # no foreign key so cant display salgrades losal and hisal columns in FrontEnd 
    
    EMSJD = Emp.objects.values('ENAME','SAL').filter(SAL__gt = Salgrade.objects.values('LOSAL').filter(GRADE =1), SAL__lt = Salgrade.objects.values('HISAL').filter(GRADE = 1))
    #<QuerySet [{'ENAME': 'SMITH', 'SAL': Decimal('800.00')}, {'ENAME': 'ADAMS', 'SAL': Decimal('1100.00')}, {'ENAME': 'JAMES', 'SAL': Decimal('950.00')}]>

    EMSJD=Emp.objects.values('ENAME','SAL').filter(SAL__gt = Salgrade.objects.values('LOSAL').filter(GRADE =2), SAL__lt = Salgrade.objects.values('HISAL').filter(GRADE = 2))
     #<QuerySet [{'ENAME': 'WARD', 'SAL': Decimal('1250.00')}, {'ENAME': 'MARTIN', 'SAL': Decimal('1250.00')}, {'ENAME': 'MILLER', 'SAL': Decimal('1300.00')}]>
    
    EMSJD=Emp.objects.values('ENAME','SAL').filter(SAL__gt = Salgrade.objects.values('LOSAL').filter(GRADE =3), SAL__lt = Salgrade.objects.values('HISAL').filter(GRADE = 3))
    #<QuerySet [{'ENAME': 'ALLEN', 'SAL': Decimal('1600.00')}, {'ENAME': 'TURNER', 'SAL': Decimal('1500.00')}]>

    EMSJD = Emp.objects.values('ENAME','SAL').filter(SAL__gt = Salgrade.objects.values('LOSAL').filter(GRADE =4), SAL__lt = Salgrade.objects.values('HISAL').filter(GRADE = 4))
    #<QuerySet [{'ENAME': 'JONES', 'SAL': Decimal('2975.00')}, {'ENAME': 'BLAKE', 'SAL': Decimal('2850.00')}, {'ENAME': 'CLARK', 'SAL': Decimal('2450.00')}]>
    
    d ={'EMSJD' :EMSJD}
    return render(request,'empSalgrade.html',d)



def updateEmp(request):
    #employee updated data
    EUP=Emp.objects.all()
    #update()
    Emp.objects.filter(ENAME = 'KING').update(ENAME='RAJA')

    Emp.objects.filter(ENAME = 'RAJA').update(SAL=50000)

    Emp.objects.filter(ENAME = 'WARD').update(JOB='CLERK')

    Emp.objects.filter(ENAME='SMITH').update(SAL =1000)


    Emp.objects.filter(ENAME='BLAKE').update(DEPTNO =20)
    
    #update_or_create()
    #update_or_create(conditions,defaults={'colName':value}

    DO =Dept.objects.get(DEPTNO =30)# Retrieve the department object
    Emp.objects.update_or_create(ENAME='SMITH',defaults={'DEPTNO':DO})#--> 1 row satisfy updates

    MO = Emp.objects.get(EMPNO= 7839) 

    Emp.objects.update_or_create(
    EMPNO=7777,
    defaults={
        'ENAME': 'RANJITHA',
        'JOB': 'MANAGER',
        'MGR': MO,
        'SAL': 75000,
        'COMM': 5000,
        'HIREDATE': '2024-05-15',
        'DEPTNO': DO
    }
)#no row satifies , so create object with defaults data , if more than 1 row satifies throws ERROR, It can handle only ONE row


    #EUP=Emp.objects.all()

    
    d={'EUP':EUP}
    return render(request,'display_emp.html',d)