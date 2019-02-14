import os
import math
import datetime


def hello(a_name):
	print("Hello!!" + a_name)

def hello2(a_name, b_name):
	print("Hello!! " + a_name + " and " + b_name)

def sum_two(x,y):
	z=x + y
	return z



def my_sum(a_list):
	total=0
	for n in a_list:
		total = total +n
	return total

def my_prod(a_list):
	total2=1
	for n in a_list:
		total2 = total2 *n
	return total2

def my_count(a_list):
	total=0
	for n in a_list:
		total= total+1 #=n/n
	return total


def my_count_less_5(a_list):
	#returns number of items<5 in a list
	count=0
	for n in a_list:
		if n < 5:
			count= count+1
	return count

def my_count_ones(a_list):
#returns number of ones in a list
	count=0
	for n in a_list:
		if n==1:
			count=count+1
	return count


def my_max(a_list):
	#return maximum value of list
	max=0
	for n in a_list:
		if n>max:
			max=n
	return max

def is_list_empty(a_list):
	if is_list_empty(a_list):
		return None
	b= a_list[0]
	for n in a_list:
		if n > b:
			b = n
	return b

#get filenames from directory
# --> list of filenames
def get_filenames(a_dirname):
	for root, dirs, files in os.walk(a_dirname):  
		for filename in files:
			print(filename)
	return  filename
get_filenames("C:/Users/dominiknitze/Desktop/pythoncode")

#get filenames from directory
# --> list of filenames
def get_filenames(a_dirname):
  list_of_files = os.listdir(a_dirname)
  all_files = []
  for filename in list_of_files:
    full_path = os.path.join(a_dirname,filename)
    if os.path.isdir(full_path): # if the file is a dir we skip it
      pass
    else:
      all_files.append(full_path)
  return all_files

def to_grayscale(an_image):
    grayscale_im=an_image.convert("L")
    return grayscale_im



#[12,34,[56,67]] -> 12 34 56 67
def flatten(a_list_with_lists):
	new_list = []
	for n in a_list_with_lists:
		if isinstance(n,list):
			for i in n:
				new_list.append(i)
		else:
			new_list.append(n)
	return new_list

#[12,34,[56,67],78] -> 
#12
#34
#5667
#78
a_list=[12,34,[56,67],78]
def print_right(a_list_with_lists):
	for n in a_list_with_lists:
		if isinstance(n,list):
			for i in n:
				print(i,end="")
			print()
		else:
			print (n)
print_right(a_list)



def single_row_stars(number):
	for n in range(0,number):
		print("*",end="")
single_row_stars(4)

def single_row_of_input(number):
	user_input=input("What do you want to print?")
	for n in range(0,number):
		print(user_input,end="")
single_row_of_input(4)
print()


def single_row_of(number,string):
	for n in range(number):
		print(string,end="")
single_row_of(4,"*")
print()
print()

def square_of_stars(num):
	for n in range(num):
		for i in range(num):
			print("*",end="")
		print()
square_of_stars(4)


def rectangle_of_stars(rows,cols):
	for n in range(rows):
		for i in range(cols):
			print("*",end="")
		print()
rectangle_of_stars(4,5)

list=[1,2,3]
def list_by_2(a_list):
	new_list1=[]
	for n in a_list:
		new_list1.append(n*2)
	print(new_list1)
list_by_2(list)


def create_grid(size):
	new_grid=[]
	for row in range(size):
		new_sublist=[]
		for column in range(size):
			new_sublist.append("-")
		new_grid.append(new_sublist)
	return new_grid
grid=create_grid(3)



list_a=[1,2,3]
list_b=[4,5,1]

def is_duplicate_there(list_a,list_b):
    for n in list_a:
        for i in list_b:
            if n == i:
				return True
	return False
is_duplicate_there(list_a,list_b)
		