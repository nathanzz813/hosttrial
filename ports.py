sql_ports = {
    "SQL Server (Microsoft)": 1433,
    "MySQL": 3306,
    "PostgreSQL": 5432,
    "Oracle Database": 1521,
    "SQLite": "No default port (usually operates on file system)",
    "MariaDB": 3306,
    "IBM Db2": 50000,
    "Firebird": 3050,
    "Sybase": 5000,
    "Couchbase": 8091,
    "Cassandra": 9042,
    "Amazon Aurora": 3306,
    "Google Cloud SQL (MySQL)": 3306,
    "Google Cloud SQL (PostgreSQL)": 5432,
    "Snowflake": 443,
}

start_instance = 1
end_instance = 5  # Adjust this based on the desired range

# Generate SAP HANA ports for the specified range of instances
sap_hana_ports = [30000 + instance * 100 + 15 for instance in range(start_instance, end_instance + 1)]

nosql_database_ports = {
    "MongoDB": 27017,
    "Cassandra": 9042,
    "Couchbase": 8091,
    "Redis": 6379,
    "Amazon DynamoDB": 443,
    "Apache HBase": 16010,
    "Neo4j": 7474,
    "RethinkDB": 28015
}

embedded_device_ports = {
    "MQTT (Message Queuing Telemetry Transport)": 1883,
    "CoAP (Constrained Application Protocol)": 5683,
    "Modbus TCP": 502,
    "SNMP (Simple Network Management Protocol)": 161,
    "BACnet (Building Automation and Control Networks)": 47808,
    "OPC UA (Unified Architecture)": 4840,
    "HTTP/HTTPS": 80, 443,
    "Telnet": 23,
    "SSH (Secure Shell)": 22,
    "FTP (File Transfer Protocol)": 21,
    "NTP (Network Time Protocol)": 123,
}

networking_device_ports = {
    "Telnet": 23,
    "SSH (Secure Shell)": 22,
    "HTTP": 80,
    "HTTPS": 443,
    "SNMP (Simple Network Management Protocol)": 161,
    "SNMP Trap": 162,
    "Syslog": 514,
    "FTP (File Transfer Protocol)": 21,
    "TFTP (Trivial File Transfer Protocol)": 69,
    "NTP (Network Time Protocol)": 123,
    "DNS (Domain Name System)": 53,
    "RADIUS (Remote Authentication Dial-In User Service)": 1812,
    "TACACS+ (Terminal Access Controller Access-Control System Plus)": 49,
    "NetFlow": 2055,
    "BGP (Border Gateway Protocol)": 179,
    "HTTPS (Web-based device management)": 8443,
}

telephone_service_ports = {
    "SIP (Session Initiation Protocol)": 5060,
    "SIPS (Secure SIP)": 5061,
    "H.323 (VoIP Protocol)": 1720,
    "MGCP (Media Gateway Control Protocol)": 2427,
    "RTP (Real-time Transport Protocol)": "Randomly assigned (commonly in the range 16384-32767)",
    "RTCP (RTP Control Protocol)": "Randomly assigned (commonly in the range 16384-32767)",
    "SCTP (Stream Control Transmission Protocol)": 2905,
    "ISDN (Integrated Services Digital Network)": 3000,
    "Cisco Skinny (SCCP - Skinny Call Control Protocol)": 2000,
    "T.38 (Fax over IP)": 49170,
}
