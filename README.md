# 🤖 Automação WhatsApp com PyWhatKit

Envie mensagens instantâneas ou agendadas para contatos e grupos no WhatsApp usando Python.

## 📌 Funcionalidades

✔ Envio instantâneo de mensagens para contatos individuais.
✔ Agendamento de mensagens com hora/minuto precisos.
✔ Suporte a envio para grupos (instantâneo ou agendado).
✔ Opções de espera e fechamento automático do navegador,

## ⚙️ Pré-requisitos

Python 3.8+

Biblioteca pywhatkit

WhatsApp Web logado no navegador padrão (Chrome/Firefox)

Número de telefone no formato internacional (ex: +5511984288699)


## 🛠️ Instalação

```
# Instale a dependência
pip install pywhatkit
```

## 📝 Como Usar


1. Mensagem Instantânea para Contato

```
import pywhatkit as kit
kit.sendwhatmsg_instantly("+5511984288654", "Olá, esta é uma mensagem instantânea!")
```

2. Mensagem Agendada para Contato

```
# Parâmetros: (número, mensagem, hora, minuto, tempo_espera, fechar_navegador, tempo_fechamento)
kit.sendwhatmsg("+5511984288654", "Mensagem agendada!", 15, 0, 10, True, 2)
```

3. Mensagem para Grupo (Agendada)

```
# Envia uma mensagem no WhatsApp com um horário específico
kit.sendwhatmsg_to_group("ID_do_Grupo", "Mensagem para o grupo!", 15, 0, 10, True, 2)
```

4. Mensagem Instantânea para Grupo

```
# Envia uma mensagem no WhatsApp com um horário específico e sem esperar
kit.sendwhatmsg_to_group_instantly("ID_do_Grupo", "Mensagem rápida para o grupo!")
```
## ⚠️ Observações Críticas

WhatsApp Web deve estar logado no navegador padrão antes de executar.

Para grupos, você precisa do GroupID (não do nome do grupo).

Evite enviar muitas mensagens em sequência para não ser bloqueado.

O parâmetro ```fechar_navegador=True``` encerra a aba após o envio.

## 🚨 Limitações

Não é uma API oficial do WhatsApp (pode parar de funcionar sem aviso).

Requer intervenção manual se houver desconexão do WhatsApp Web.