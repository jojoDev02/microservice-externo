# microservice-externo

Este microservice foi desenvolvido como parte da disciplina Engenharia de Software II, com o objetivo de integrar o sistema Vá de Bike com APIs externas. O projeto segue os princípios da Clean Architecture, garantindo uma estrutura modular e de fácil manutenção.

**Ci-CD Pipeline**

Implementamos uma pipeline de CI-CD para garantir a qualidade do código e automatizar o processo de entrega. A pipeline inclui as seguintes etapas:

**Testes Automatizados:** São executados testes automatizados para verificar a integridade e funcionalidade do microservice.

**Análise Estática com Sonar Cloud:** Utilizamos o Sonar Cloud para realizar uma análise estática do código, identificando possíveis problemas de qualidade e padrões de codificação.

**Deploy na GCP (Google Cloud Platform):** Após os testes e a análise estática, o microservice é automaticamente implantado no serviço Cloud Run da GCP. Isso proporciona uma maneira escalável e eficiente de disponibilizar o microservice na nuvem.
