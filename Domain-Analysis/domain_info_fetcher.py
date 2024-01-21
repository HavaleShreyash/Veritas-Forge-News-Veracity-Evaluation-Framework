import whois

def get_domain_info(domain_name):
    try:
        domain_info = whois.whois(domain_name)
        return domain_info
    except whois.parser.PywhoisError as e:
        print(f"Error fetching information for {domain_name}: {e}")
        return None
    
def get_nameservers(domain_name):
    try:
        domain_info = whois.whois(domain_name)
        return domain_info.name_servers
    except whois.parser.PywhoisError as e:
        print(f"Error fetching information for {domain_name}: {e}")
        return None

if __name__ == "__main__":
    # Example usage:
    domain_name = "whois.google.com"
    domain_info = get_domain_info(domain_name)
    nameservers = get_nameservers(domain_name)

    if domain_info:
        print(f"Domain Name: {domain_info.domain_name}")
        print(f"Registrar: {domain_info.registrar}")
        print(f"Creation Date: {domain_info.creation_date}")
        print(f"Name Servers: {', '.join(domain_info.name_servers)}")
        print(f"Admin Organization: {domain_info.admin_organization}")
        print(f"Tech Organization: {domain_info.tech_organization}")
        print(f"Registrant Organization: {domain_info.registrant_organization}")
    else:
        print(f"Unable to fetch information for {domain_name}")
    
    # if nameservers:
    #     print(f"Name Servers for {domain_name}: {', '.join(nameservers)}")
    # else:
    #     print(f"Unable to fetch Name Servers for {domain_name}")