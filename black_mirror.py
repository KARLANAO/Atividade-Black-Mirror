# Perguntas e Respostas 

perguntasRespostas = {
  "Qual é o nome completo da protagonista do episódio?": "Joan Tait",
  
  "Quem dirige a vida de Joan em tempo real para uma série de televisão?": "Um computador quântico e as cenas da série é gerada em CGI",
  
  "Qual é o nome do serviço de streaming fictício que parodia a Netflix no episódio?": "Streamberry",
  
  "Qual música Joan dubla enquanto dirige para o trabalho?": "",
  
  "Por que Joan demite Sandy e qual era o papel de Sandy na empresa?": "",
  
  "Quem são os dois atores que interpretam Joan e Krish na série dentro do episódio?": "Selma Hanks"
  
  "Como Joan descobre a existência da série sobre sua vida?" "Assistindo TV com o noivo Krish.", 
  
  "Qual é a reação inicial de Joan ao descobrir a série e o que ela faz em resposta?": "Joan surta e tenta processar a empresa.",
  
  "Quais são os temas principais explorados neste episódio de Black Mirror?": "O episódio fala sobre captação de dados, consentir permissões de uso sem ler, inteligência artificial, deep fake, privacidade",
  
  "O episódio termina de maneira típica para a série Black Mirror? Explique.": "Não posso opinar pois não assisto a série."
}


pergunta = input("Faça uma pergunta sobre o episódio de Black Mirror: ")

# Verifica se a pergunta está no dicionário e exibe a resposta correta 

if pergunta in perguntasRespostas:
    print("Resposta:", perguntasRespostas[pergunta])
else:
    print("Desculpe, não tenho uma resposta para essa pergunta.")
