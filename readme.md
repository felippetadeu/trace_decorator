Versão do Python utilizada 3.10

Esse projeto foi criado com o objetivo de testar e aprender sobre criação de comportamentos em runtime


O decorator criado para estudo tem a finalidade de injetar o método `__getattribute__` para que possa ser rastreada a utilização de métodos que não seja da classe `object` e que não sejam os métodos listados na constante `LIST_OF_DEFAULT_METHODS`