Provisinamento de um novo site
=======

## Pacotes necessários
* nginx
* Python 3.6
* virtualenv + pip
* Git

Por exemplo, no Ubuntu
	sudo add-apt-repository ppa:fkrull/deadsnakes
	sudo apt-get install nginx git python36 python3.6-venv

## Config no Nginx Virtual Host
* Veja nginx.template.conf
* substitua SITENAME, por exemplo, por staging.my-domain.com

## Serviço Systemd
* veja gunicorn-systemd.template.service
* substitua SITENAME, por exemplo, por staging.my-domain.com
* 
## Estrutura de pastas:
Suponha que temos uma conta de usuário em /home/username

```bash
/home/username
└── sites
	└── SITENAME
		 ├── database
		 ├── source
		 ├── static
		 └── virtualenv
```
