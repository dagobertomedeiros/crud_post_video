# crud_post_video
## Teste CRUD Python com PyQt5 e MongoDB

Aplicação construída como um monolíto. Utilizando o conceito da arquitetura MVC.
Toda a implementação foi realizada utilizando PyQt5 e Python 3.10
Sua execução é muito simples, bastando apenas executar o arquivo na raiz do projeto app.py,
tal execução pode ser diretamente pelo terminal ou mesmo utilizando uma venv.

Ressalvas:
- Houve problemas com a instalação do MongoDB no PC, por isso não pude fazer o CRUD com o BD, já tinha tomado nota
de como funciona a autenticação, consultas e inserções, todavia, há algum problema com a versão do Ubuntu que estou 
utilizando, tentei até usar uma instância via docker, porém não foi trivial e me consumiu muito tempo sem garantir o
sucesso esperado. Todo esse esforço comprometeu parte das tarefas pretendidas, inclusive o login via middleware, que 
se quer houve tempo hábil para escolher e implementar.
- Apesar dos percalços, espero que gostem do código, tentei escrever dentro das melhores práticas possíveis. Notará que há verificação da escrita do código com Pylint e, também um exemplo de teste unitário. Além disso, utilizei os recursos no github actions para rodar pipelines que verificam o código e sua escrita, inclusive com testes em 3 versões do python.
- Em virtude da dificuldade exposta com o MongoDB, o player possui apenas um arquivo de video para teste de execução,
pode notar que sua reprodução é simples, basta clicar no botão com sinal de "+", em seguida clica no botão play. Lembrando que o login é "Chico" e a senha "1234".

Importante: Para sua execução é importante possuir o PyQt5 instalado, para isso basta no terminal de seu computador
[pip install pyqt5].
