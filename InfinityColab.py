from selenium import webdriver
import random
import pyperclip
import time

##############################################################################################################################

def main():

	print('\033[36m' '''                                                                                                                                                                                                                                                                                    
                                               .&@&&&&&&&&&&&@@@@/                                                                                                          
                                           ,@&&&&&&&&&&&&&&&&&&&&@@@&&@(                                                                                                    
                                       .&@&&&&&&&&&&&&@&&&&@@@@@@@@@@@&&&&&@&*,                                                                                             
                                  .%@@@@&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&@#,                                                                                         
                              ,&@@@@@@@&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&@(                                                                                      
                          .&@@@@@@@@@@&&&@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@&&@@@@@&&&&                                                                                    
                       .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&@@@&&&&&@                                                                                  
                     ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@&.                                                                                
                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/                                                                               
                   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.                                                                              
                  /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                                                              
                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.                                                                             
                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#                                                                             
                  @@@@@@@&(@@@@@@@@@@@@@@@@@@@&%((((((/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                                                             
                 .@@@@@@#//@@@@@@@@@@@@&/////////////((#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                                                             
                 ,&@@(&@@%///#@@@@@@@(/////////////////((@@@@@@@@@@@@@@@@@@@&%(((///%@@@@@@@@@@                                                                             
                  @@///@@@&//////((////////*************////((((////////////*//********/@@@@@@@                                                                             
                  &//*/*%&&////////////*************************************************%&&@@@@                                                                             
                  %/***************************************************************,,***#&&&@@%                                                                             
                 .#******************************************************************,**#&&&&@.                                                                             
                 @******************************************,***,***************,***,,**%%&&&@                                                                              
                .&**************************************************,*******************(%&&&@                                                                              
                @#********************************************,,,,**,,,,,,,,,,,*,***,****%%%&(                                                                              
               .@/***#@@@@@@@@@@@&/*********************************,,/(##(*,,,,*,,*******%%&                                                                               
          (,**,/%***@@@@@@@@@@@@@@@@@@@#*********************#&@@@@@@@@@@@@@@@@@*,,********&@                                                                               
         /%%%%&******////******//#&@@@@@@@@@#***********%@@@@@@@@@@@@@&%###%&@@@@@*,*******@*                                                                               
         %/#(**/%***//*/*/**/((//**/*/((((((////*******//////////****************%@&******#&*,,                                                                             
         #*//***(****//((#@@@%@@@@@&@@##(((((//********//////***(%%%%%%%#/****************%&***,*,(                                                                         
         ,**/***(**********////#%%%%*(((((((//**.,,,,,*//***((%&%&@@@@@@#(///(***********(****%%%%*#,                                                                       
          %*%**%**************************///**,,,,,,,********/((/&&&&@,./(&#/***********(*(*,**#%*#,                                                                       
          ./*%*//*****************************,,,,,,,,,,********************************/*(***,*%%*%                                                                        
           ***%*#****************************,,.,,,,,,,,,,,,,,***************,,,,,******////**,*%%*,                                                                        
             %,,%***************************,,,.,,,,,,,,,,,,,,,,****,,***,,,,,,,,,,,***&//%%#**/%/,                                                                         
               %&**************************,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*,,,,,,,,*****(&*/##*,**&                                                                           
                @(*************************,,,,,,,,,,,,,*,,,,,,,,,,,,,,******,,*******&&******(                                                                             
                @@*******************/*******, ,,,,,,,,,,(,,,,,,,,,,,,*,,************&@,*,,**.                                                                              
                @@*******************///(//************,,*,*,**,,,,,,,*,,,**,***,***&@#,,,#                                                                                 
                @@&********************(%%(#(////#%%%&&//*,*******,,,,,,,,,********&&@(                                                                                     
                %@@#******************#&&&@@(////(%&#*,*************,,,,,,,,,*****%&&@                                                                                      
                .@@&(********%&&&&&&@@&&&&&&&&&&&&&&&&&&*,,,,,,*****,,,,,,,,****/&&&&&                                                                                      
                 (@@&(/*****&&&&&@&&&&&@&&&&&&&&&&&&@@@@@@&&@&&,****,*,,,,,*,**%%&&&@                                                                                       
                  @@@&(///*/&&@&&&&/((#(/#&&@@@@&&@@@@@@@@@@@@@&&&***********/%%&&&@                                                                                        
                   @@&&&///*(&***//#####%%&%(//**///**(&@@@@@@@@&&&*********%%%&&&&%*/                                                                                      
                    @@@&&%///*******/(((((((############%###(@@&&&#*******(%&&&&&&@/,..(                                                                                    
                     &@@@&&&&**********/(((((((((((((((/*****/(&&*******%%&&&&&&&@/%    /                                                                                   
                      *@@@@&&&(******/*#&&%#(///*********************%&%&&&&&&&@@/       *                                                                                  
                        @@@@&&&%******/(&&&&&&&&&&&#************#%%&&&&&&&&&&@@.          ,                                                                                 
                         @@@@&&&%*******//&&&&&&&&&***********%%%&&&&&&&&&&@&              .                                                                                
                          /@@@&&&&/*********#%%/************(%&&&&&&&&&&&@,                 .                                                                               
                            @@@&&&&&&&&%####/************(%%&&&&&&&&&&@( .                   ,                                                                              
                             #@@&&&&&&&&&&&&&&&%%%%%%%%%%&&&&&&&&&@@(.                         ,                                                                            
                              */@@&&&&&&&&&&&&&&&&&%%&&&&&&&&&@@@... .                            ,                                                                         
                            *./(((#@@&&&&&&&&&&&&&&&&&&&&&@@@,...... .                                ,.                                                                    
                       *.     (//((((((#@@@@@@@@@@@@@@@@/...........                                  **,,*                                                                 
             /,/,,.., ,.  ..  #*/(((((((((((((#%(,,,,..............                               .%*,,,,,,,,,*                                                             
          *   *,*****...,,,. ..(//////(((((##*,,,,............... .               ...           /(********,,,,,,,#                                                          
       *     ,.*******,/,,,.  .*/**%///*&*,................. ....                ,            (/************,,,,,,,,/,                                                      
     ,       ,.***********.. .  #///////**%................. .                ..            (/****************,,(#.      .*                                                 
   ,          /**********,,,*..,//////////*/&............                   ,             ,(******************#              ,                                              
  ,            /****,**//*,,,,,%***/////(&(//((...... ..    .            ,.              %*****************(*                 ..                                            
,             .////////*///**,**@@@@@@@@&&&&#/&. .                    ,               //****************#.                       ,*,                                       
.            ,,,,/((//////////%&&&&(*////*//////**. .               ..                %************(/*/#.                                 ,*,                               
.          ,,,,*,   ,(///****&&%**%&&&&@@@&@@&&&&&&%              ,                 ((*********(###((#.                                           ,*                        
         ,,****        ,#%%#*,.......#@////////*#(*&.          ,.                 .%/********####//(                                                    *.                  
       ,,****,            ..        ....*@(/////**%%.. .    .*                   #(*******/####/#(.                                                         *,              
     .,,***/                     .        ./&///*#%(.*   ./.                   *#(******//(#/*((.                                                              *            

''')

	print('\033[0m''\033[1m' "Olá Jean! Como vai?! Estou iniciando o sistema pra você...")

	print("""
		""")

	print(" Iniciando automação... ")

	print("""
		""")

	logincolaborador()

##############################################################################################################################

def logincolaborador():

	global navegador

	global categoria

	global repetir

	global abainfinity

	global escolheupormim

	global pagina

	global conteudopaginah

	global conteudopaginav


	categorias = input("""Qual categoria quer adicionar? (Somente Números)

		x - Decida por mim | 1 - Informática | 2 - Idiomas | 3 - Educação | 4 - Design | 5 - Negócios | 6 - Música | 7 - Outros 

		""")

	repetir = int(input("""Jean gostaria de adicionar somente um conteúdo, ou quer repetir a operação várias vezes? (Somente Números)

		1 - Adicionar só um conteúdo | 2 - Repetir Infinitamente 

		"""))

	pagina = int(input("""Em qual página da categoria """ + str(categorias) + """ devo acessar os conteúdos Jean? (Somente Números)

		Entre 1 a 100

		"""))

	conteudopaginah = int(input("""Eu devo acessar qual conteúdo da página """ + str(pagina) + """ ? (Somente os números 1, 2 ou 3)

		Selecione o conteúdo | 1 |, | 2 | ou | 3 | para o sentido horizontal da página! 

		"""))

	conteudopaginav = int(input("""Eu devo acessar qual conteúdo da página """ + str(pagina) + """ ? (Somente os números 2, 3, 4 ou 5)

		Selecione o conteúdo | 2 |, | 3 |, | 4 | ou | 5 | para o sentido vertical da página! 

		"""))

	print("""Ótimo! Então farei o login na plataforma de colaborador e adicionarei os conteúdos para você!

			Agora é tudo comigo mestre! Você já gastou tempo de mais me programando!

			Aguarde...
			""")

	time.sleep(1)


	if categorias == "1" or categorias == "2" or categorias == "3" or categorias == "4" or categorias == "5" or categorias == "6" or categorias == "7":

		categoria = categorias

		escolheupormim = "n"

	elif categorias == "x":

		categoria = categorias

		escolheupormim = "s"

	else:

		erro()


	navegador = webdriver.Chrome()

	navegador.maximize_window()

	navegador.get("https://eadinfinity.com/colaborador/")

	time.sleep(1)

	navegador.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div[4]/form/div[1]/input').send_keys("jean@eadinfinity.com")

	navegador.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div[4]/form/div[2]/input').send_keys("124578")

	navegador.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div[4]/form/button').click()

	time.sleep(1)

	abainfinity = navegador.current_window_handle

	navegador.switch_to.new_window('tab')

	iniciar()


##############################################################################################################################

def iniciar():

	global categoria

	global abacursou

	global pagina

	global conteudopaginah

	global conteudopaginav

	
	if escolheupormim == "s":

		categoria = int(random.randrange(1, 7))


	if conteudopaginav == 4 and conteudopaginah == 4:

		pagina += 1

		conteudopaginav = int(2)

		conteudopaginah = int(1)

	else:


		if conteudopaginah == 4:

			conteudopaginav += 1

			conteudopaginah = int(1)

	
	listacategoria = ["", "informatica", "idiomas", "educacao", "design", "administracao", "musicas", "concursos"]

	navegador.get("https://www.cursou.com.br/" + listacategoria[int(categoria)] + "/page/" + str(pagina))

	abacursou = navegador.current_window_handle

	propaganda = navegador.find_element_by_xpath('/html/body/main/div/div[3]/div[1]/div[2]/div/div[' + str(conteudopaginav) + ']/div[' + str(conteudopaginah) + ']/div/a').get_attribute("href")

	navegador.find_element_by_xpath('/html/body/main/div/div[3]/div[1]/div[2]/div/div[' + str(conteudopaginav) + ']/div[' + str(conteudopaginah) + ']/div/a').click()


	while navegador.current_url != propaganda:

		navegador.get("https://www.cursou.com.br/" + listacategoria[int(categoria)] + "/page/" + str(pagina))

		time.sleep(1)

		navegador.find_element_by_xpath('/html/body/main/div/div[3]/div[1]/div[2]/div/div[' + str(conteudopaginav) + ']/div[' + str(conteudopaginah) + ']/div/a').click()

		time.sleep(1)

			

	print("""
		Abaixo estão algumas informações inportantes sobre o processo!
			""")

	print("Categoria:")

	print(listacategoria[int(categoria)])

	print("____________")

	print("Página:")

	print(pagina)

	print("____________")

	print("Horizontal:")

	print(conteudopaginah)

	print("____________")

	print("Vertical:")

	print(conteudopaginav)

	print("____________")

	
	preparar()


##############################################################################################################################

def preparar():

	time.sleep(1)

	titulocurso = navegador.find_element_by_xpath('/html/body/div[2]/div/main/div/div[1]/h1').text

	titulocurso = titulocurso.replace('Curso de ', '')

	titulocurso = titulocurso.lower().capitalize()

	professor = navegador.find_element_by_xpath('/html/body/div[2]/div/main/div/div[1]/div[4]/ul/li[1]').text

	professor = professor.replace('Empresa: ', '')

	professor = professor.replace('Professor: ', '')

	nivel = navegador.find_element_by_xpath('/html/body/div[2]/div/main/div/div[1]/div[4]/ul/li[2]').text

	sobre1 = navegador.find_element_by_xpath('/html/body/div[2]/div/main/div/div[1]/p[1]').text

	sobre2 = navegador.find_element_by_xpath('/html/body/div[2]/div/main/div/div[1]/p[2]').text

	sobre = str(sobre1 + sobre2)

	time.sleep(1)

	navegador.switch_to.window(abainfinity)

	navegador.find_element_by_xpath('//*[@id="menu"]/li[3]/a').click()

	time.sleep(1)

	navegador.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div/div/div/form/div/div[1]/div[1]/div/input').send_keys(titulocurso)

	navegador.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div/div/div/form/div/div[1]/div[2]/div/input').send_keys(professor)

	if nivel == "Nível do curso: Básico":

		navegador.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div/div/div/form/div/div[1]/div[3]/div/select').click()

		navegador.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div/div/div/form/div/div[1]/div[3]/div/select/option[1]').click()
	
	elif nivel == "Nível do curso: Intermediário":

		navegador.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div/div/div/form/div/div[1]/div[3]/div/select').click()

		navegador.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div/div/div/form/div/div[1]/div[3]/div/select/option[2]').click()

	elif nivel == "Nível do curso: Avançado":

		navegador.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div/div/div/form/div/div[1]/div[3]/div/select').click()

		navegador.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div/div/div/form/div/div[1]/div[3]/div/select/option[3]').click()

	else:

		print("Erro na ( preparar ) | nivel")

		erro()

	if categoria == "1":

		navegador.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div/div/div/form/div/div[2]/div[1]/div/select').click()

		navegador.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div/div/div/form/div/div[2]/div[1]/div/select/option[1]').click()

	elif categoria == "2":

		navegador.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div/div/div/form/div/div[2]/div[1]/div/select').click()

		navegador.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div/div/div/form/div/div[2]/div[1]/div/select/option[2]').click()

	elif categoria == "3":

		navegador.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div/div/div/form/div/div[2]/div[1]/div/select').click()

		navegador.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div/div/div/form/div/div[2]/div[1]/div/select/option[3]').click()

	elif categoria == "4":

		navegador.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div/div/div/form/div/div[2]/div[1]/div/select').click()

		navegador.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div/div/div/form/div/div[2]/div[1]/div/select/option[4]').click()

	elif categoria == "5":

		navegador.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div/div/div/form/div/div[2]/div[1]/div/select').click()

		navegador.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div/div/div/form/div/div[2]/div[1]/div/select/option[5]').click()

	elif categoria == "6":

		navegador.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div/div/div/form/div/div[2]/div[1]/div/select').click()

		navegador.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div/div/div/form/div/div[2]/div[1]/div/select/option[6]').click()

	elif categoria == "7":

		navegador.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div/div/div/form/div/div[2]/div[1]/div/select').click()

		navegador.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div/div/div/form/div/div[2]/div[1]/div/select/option[7]').click()

	else:

		print("Erro na ( preparar ) | categoria")

		erro()


	navegador.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div/div/div/form/div/div[2]/div[2]/div/textarea').send_keys(sobre)

	time.sleep(1)

	navegador.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div/div/div/form/div/div[2]/div[3]/div/button').click()

	time.sleep(1)

	print("_")

	print(titulocurso + " / " + professor + " / " + nivel)

	print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

	print("_")

	adicionar()


##############################################################################################################################

def adicionar():

	global conteudopaginah


	navegador.switch_to.window(abacursou)

	lista = []

	listaaulas = navegador.find_element_by_id("lista-aulas")

	aulas = listaaulas.find_elements_by_tag_name("a")

	time.sleep(1)


	for aula in aulas:

		lista.append(aula.text)

	tamanhodalista = len(lista)

	contador = -1

	time.sleep(1)


	for x in range(0, tamanhodalista):

		contador += 1

		navegador.switch_to.window(abainfinity)

		navegador.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div[1]/div/div/div/form/div/div[1]/div[1]/div/input').send_keys(lista[contador])

		navegador.switch_to.window(abacursou)

		navegador.find_element_by_link_text(lista[contador]).click()

		time.sleep(3)

		player = navegador.find_element_by_xpath('//*[@id="player"]')

		time.sleep(1)

		webdriver.ActionChains(navegador).context_click(player).perform()

		time.sleep(1)

		navegador.switch_to.frame(player)

		time.sleep(1)

		playervideo = navegador.find_element_by_xpath('/html/body/div[2]/div/div/div[4]')

		playervideo.click()

		urlinteira = pyperclip.paste()

		url = urlinteira[39:80]

		navegador.switch_to.default_content()

		navegador.switch_to.window(abainfinity)

		navegador.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div[1]/div/div/div/form/div/div[2]/div[1]/div/textarea').send_keys(url)

		time.sleep(1)

		navegador.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div[1]/div/div/div/form/div/div[2]/div[2]/div/button').click()

		time.sleep(1)

		print(lista[contador])

		print("-------------------------------------------------------------------------------------------------------")
		
		print(url)

		print("########################################################################################################")

		print("_")


	if repetir == 2:

		navegador.switch_to.window(abacursou)

		conteudopaginah += 1

		navegador.get("https://www.youtube.com/watch?v=2_xBCeBmaS8")

		time.sleep(10)

		iniciar()


##############################################################################################################################

def erro():

	print("""

		<= ERRO => (Alguma coisa saiu errado Jean. Por favor, me concerte!

		Vou tentar reiniciar o sistema... Aguarde...

		""")

	webdriver.Chrome().quit()

	time.sleep(7)

	main()

##############################################################################################################################

if __name__ == '__main__':

	main()