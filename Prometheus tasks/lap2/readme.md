1-How do I trigger a Prometheus alert?

	- Setup and configure AlertManager.
	- Configure the config file on Prometheus so it can talk to the AlertManager.
	- Define alert rules in Prometheus server configuration.
	- Define alert mechanism in AlertManager to send alerts via Slack and Mail

2-What is the difference between node exporter and mysql exporter ?

	- Node exporter:
		- collects metrics from linux based systems
		- port 9100
	- Mysql exporter:
		- collects metrics from mysql database
		- port 9104

3-what is the maximum retention period to save data in Prometheus and how to increase it ?
	
	- The default is 15 days
	- increase the retention time to a year
	  >> --storage.tsdb.retention.time=1y

4-What are the different PromQL data types available in Prometheus Expression language?

	- PromQL uses three data types: 
		- scalars
		- range vectors
		- instant vectors
	- It also uses strings, but only as literals

5-How To calculate the average request duration over the last 5 minutes from a histogram ?

	>> rate(http_request_duration_seconds_sum[5m])
		or
	>> rate(http_request_duration_seconds_count[5m])

6-What is Thanos Prometheus?

	Thanos is a set of components that can be composed into a highly available metric 
	system with unlimited storage capacity, which can be added seamlessly on top of 
	existing Prometheus deployments.

7-what is promtool and how i can use it ?

       - Tooling for the Prometheus monitoring system.
       - SYNOPSIS:
       		>> promtool [<flags>] <command> [<args> ...]
       - COMMANDS:
       		>> check config <config-files>...
       		=> Check if the config files are valid or not.

   		>> check web-config <web-config-files>...
       		=> Check if the web config files are valid or not.

   		>> check rules <rule-files>...
       		=> Check if the rule files are valid or not.

8-What types of Monitoring can be done via Grafana?

	- infrastructure and log analytics

9-Can we see different Servers CPU comparison in Grafana

	Yes, it is definitely possible
	by making different query of each server
