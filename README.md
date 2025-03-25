**README - Script de Ataque DoS (SYN Flood + HTTP Flood)**

---

### **Descrição**

Este script realiza um ataque **DoS** combinando duas técnicas:
1. **SYN Flood**: Envia pacotes TCP SYN falsificados para sobrecarregar as conexões do servidor.
2. **HTTP Flood**: Envia um grande volume de requisições HTTP simultâneas para sobrecarregar a capacidade do servidor web.

**⚠️ ATENÇÃO:**
- Este script é **estritamente para fins educacionais** ou **testes de segurança autorizados** em ambientes controlados.
- **Realizar este tipo de ataque sem a permissão do proprietário do sistema é ilegal e pode levar a processos legais.**

---

### **Pré-Requisitos**

1. **Python 3.x**
2. **Bibliotecas**:
   - `scapy` (para o SYN Flood)
   - `aiohttp` (para o HTTP Flood)
   - `threading` e `asyncio` (para paralelismo e concorrência)

#### Instalar as dependências:

```bash
pip install scapy aiohttp
```

---

### **Como usar o script**

1. **Configuração do alvo**:  
   Antes de executar, altere as variáveis **`IP_ALVO`** e **`URL`** para o IP e o URL do alvo que você deseja testar.

   - `IP_ALVO`: IP do servidor alvo para o ataque **SYN Flood**.
   - `URL`: URL completa (ex: `http://example.com`) para o ataque **HTTP Flood**.

2. **Rodando o script**:

   O script irá rodar simultaneamente os dois tipos de ataque:
   - **SYN Flood** com múltiplas threads.
   - **HTTP Flood** com múltiplas requisições assíncronas.

   Para iniciar o ataque, basta rodar o script:

   ```bash
   python script.py
   ```

   O ataque **SYN Flood** será disparado com o número de threads definido na função `iniciar_syn_threads()`, e o **HTTP Flood** será executado com o número de requisições simultâneas definidas na função `iniciar_http_flood()`.

---

### **Estrutura do Código**

- **Função `syn_flood()`**: Envia pacotes TCP SYN falsificados para o servidor alvo.
- **Função `http_flood()`**: Envia requisições HTTP GET simultâneas ao servidor alvo.
- **Função `iniciar_syn_threads()`**: Cria e gerencia as threads para o ataque SYN Flood.
- **Função `iniciar_http_flood()`**: Gerencia a execução do HTTP Flood usando `asyncio`.

---

### **Avisos Importantes**

- **Uso autorizado**: Só execute este script em ambientes que você tenha autorização para testar, como servidores próprios ou com permissão explícita do proprietário.
- **Consequências legais**: Atacar sistemas sem permissão é um crime. O uso deste script de forma mal-intencionada pode resultar em responsabilidade legal.
- **Responsabilidade do usuário**: O uso deste código é de sua própria responsabilidade. O criador deste script não se responsabiliza por qualquer uso indevido ou ilegal do código.

---

### **Licença**

Este código é fornecido para fins educacionais sob a **Licença MIT**. Você pode usá-lo, modificar e distribuí-lo, desde que não seja utilizado para fins ilegais.

---

### **Contato**

Se você tiver dúvidas sobre o uso legítimo de técnicas de segurança ou quiser aprender mais sobre **defesa contra ataques DoS**, entre em contato com profissionais de **cibersegurança** ou consulte fontes confiáveis.

---
