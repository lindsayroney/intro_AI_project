for target_param, local_param in zip(target_net.parameters(), local_net.parameters()):
    target_param.data.copy_(tau*local_param.data + (1.0-tau)*target_param.data)
