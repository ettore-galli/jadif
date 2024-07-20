# DEMO

## Local setup

Demo local setup must be done manually, since its requirements are no part of the jadif project's.

### Install python dependencies

```shell
pip in stall -r demo_requirements.txt
```

### Startup Database

```shell
demo/database/start-db.sh
```

### Run

### Start the importer

```shell
export PYTHONPATH=. # una tantum

# Version *without* Dependency Injection
python demo/main_no_di.py demo/configuration/config.ini

# Version *with* Dependency Injection
python demo/main_di.py demo/configuration/config.ini
```

### Check the result

```sql
select * from import_data id;
```
