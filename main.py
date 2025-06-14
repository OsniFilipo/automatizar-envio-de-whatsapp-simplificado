# Importando a biblioteca pywhatkit para enviar mensagens no WhatsApp
import pywhatkit as kit 

# Envia uma mensagem instantânea no WhatsApp simples
kit.sendwhatmsg_instantly("+5511984288654", "Teste de mensagem !")

# Envia uma mensagem no WhatsApp com um horário específico
kit.sendwhatmsg("+5511984288654", "Teste de mensagem agendada !", 15, 0, 10, True, 2)

# Envia uma mensagem no WhatsApp com um horário específico e sem esperar
kit.sendwhatmsg_to_group("Grupo de Teste", "Teste de mensagem para grupo !", 15, 0, 10, True, 2)

# Envia uma mensagem no WhatsApp com um horário específico e sem esperar
kit.sendwhatmsg_to_group_instantly("Grupo de Teste", "Teste de mensagem para grupo !")