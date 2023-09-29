# mysql_cloudmanaged_databases

## GCP Setup Process
1. Log into `console.cloud.google.com`.
2. Click on `'Select a project` in the upper left side of the screen and click on `New Project`. Fill in the information and click `Create`.
3. In the navigation menu on the left side of the screen, click on `SQL`.
4. Click on `Create Instance`. Choose `MySQL` and click `Next`, and then `Enable API`.
5. When creating the MySQL instance, create a password for the `root` user. Then changed the configuration options. Click `Create` to start the deployment.
6. Once the instance is created, open `MySQL Workbench` and create a new connection. Use the IP address of the instance as the hostname, and use the `root` user and password created earlier. the IP address can be found in the `Overview` tab of the instance. Click `OK` to connect.

## Azure Setup Process
1. Log into `portal.azure.com`.
2. Click on `Create a resource` in the upper left side of the screen and click on `Databases` and then `Azure Database for MySQL`, and `Flexible server`. Fill in the information and click `Create`.
3. Change the default configuraton options to  `Burstable`, `B1s`, `1 vCores`, `1 GiB RAM`, and `20 GiB storage`. Click `Review + create` and then `Create`.
4. Once the instance is created, open `MySQL Workbench` and create a new connection. Use the IP address of the instance as the hostname, and use the `root` user and password created earlier. the IP address can be found in the `Overview` tab of the instance. Change the username from `root` to the server admin name. Click `OK` to connect.
