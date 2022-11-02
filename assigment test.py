# #1.Ans
# a=10
# b=20
# a,b=b,a
# print(a)
# print(b)

# #2.Ans
# 1.overloading-overloding method having same name but diffrent parameter are passed
# types.1.operator overloading
#     2.constructor overloading
#     3.method overloading


# 2.overriding- In overriding method Parent Class method is defined in Child class and it ovverrride by child class .

# class A:
#     def m1(self):
#         print('m1--- called')

# class B(A):
#     def m2(self):
#         print('m2---called')

#     def m1(self):
#         print('m1----B')

# b=B()
# b.m1()


# 3.Write a program to find the second largest number in an array
# l=[1,2,3,4]
# def m1(x):
#     f_max=max(l[0],l[1])
#     s_max=min(l[0],l[1])
#     for i in range(2,len(l)):
#         if l[i]>f_max:
#             s_max=f_max
#             f_max=l[i]
#         else:
#             l[i]>s_max and f_max!=l[i]
#             s_max=l[i]
#     return s_max

# print(m1(l))

# 5.
data = [-2, 4, 0, 1, -9]


def bubblesort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[i]
                array[j] = array[j + 1]
                array[j + 1] = temp


(bubblesort(data))
print(data)

# #8.Ans
# select FIRST_NAME,LAST_NAME ,count(DEPARTMENT_ID) as DEPARTMENT_ID GROUP_BY (DEPARTMENT_NAME,MANAGER_ID)
# from employee where departments ='USA';

# #9.
# select FIRST_NAME,LAST_NAME ,Avg(salary)>salary from employee where departments='IT';


# #11
# select salesman_id,name,city,commission ,customer_id,name from salesman ,customer where city='london';
# or
# select salesman_id,name,city,commission ,customer_id,name from salesman
# inner join customer
# on salesman_id.name = customer_id.name;

# 12.Design schema for products' order database

create table products(
    product_id int primary_key=True,
    product_name varchar(150),
    prise varchar(150)
    );
create table order(
    order_id int ,
    order_name varchar(150),
    fk_id int foregin key order(order_id) references product (product_id) on update cascade on delete casacade
    );
