def topla(x,y):
	return x + y
def çıkar(x,y):
	return x - y
def böl(x,y):
	return x / y
def çarp(x,y):
	return x * y

while True:	
	try:
		ilksayı=int(input("İlk sayıyı giriniz: "))
	except:
		print("Lütfen Sayı Gir!!")
	try:	
		ikincisayı=int(input("İkinci sayıyı girinz: "))
	except:
		print("Lütfen Sayı Gir!!")
	try:	
		işlem=input("Yapmak İsteğiniz İşlem Nedir? (*,/,+,-) : ")
	except:
		print("Lütfen Geçerli işlem Gir!!")
		
	if işlem == "+":

		print(ilksayı,"+",ikincisayı,"=",topla(ilksayı,ikincisayı))

	elif işlem == "-":

		print(ilksayı,"-",ikincisayı,"=",çıkar(ilksayı,ikincisayı))

	elif işlem == "/":

		print(ilksayı,"/",ikincisayı,"=",böl(ilksayı,ikincisayı))

	elif işlem ==	"*":

		print(ilksayı,"*",ikincisayı,"=",çarp(ilksayı,ikincisayı))

	else:

		print("Düzgün Gir Lan İşlemi :D")



