Explicação do SOLID no projeto

SRP (Single Responsibility Principle): Cada classe tem uma única responsabilidade. PersonagemModel lida com o mapeamento do banco de dados, PersonagemRepository lida com operações de banco de dados, PersonagemService lida com lógica de negócios, e o controlador lida com rotas e endpoints.

OCP (Open/Closed Principle): PersonagemService pode ser estendido com novas funcionalidades sem modificar a implementação existente. Podemos criar subclasses ou adicionar novos métodos sem alterar o código original.

LSP (Liskov Substitution Principle): As subclasses e as classes dependentes mantêm o comportamento da classe base. Isso garante que substituições de dependências não quebrem o sistema.

ISP (Interface Segregation Principle): Dividimos a responsabilidade em várias interfaces (repositorio, serviço, controlador) em vez de uma única interface geral.

DIP (Dependency Inversion Principle): PersonagemService depende de abstrações (PersonagemRepository) em vez de concretizações. Usamos injeção de dependência para passar a instância do repositório para o serviço.