```bash
chmod +x backend/entrypoint.sh
```

```
dcm exec backend pytest tests -k pizza
```

```bash
    echo "docker-compose exec backend pytest . -p no:warnings"
    docker-compose exec backend pytest . -p no:warnings
    ;;    
"testcov")
    echo "docker-compose exec backend pytest . -p no:warnings --cov=\"app\""
    docker-compose exec backend pytest . -p no:warnings --cov="app"
    ;;        
"flake8")
    echo "docker-compose exec backend flake8 ."
    docker-compose exec backend flake8 .
    ;;    
"blackc")
    echo "docker-compose exec backend black . --check"
    docker-compose exec backend black . --check
    ;;
"black")
    echo "docker-compose exec backend black ."
    docker-compose exec backend black .
    ;;
"sortc")
    echo "docker-compose exec backend /bin/sh -c \"isort app/*/*.py --check-only\""
    docker-compose exec backend /bin/sh -c "isort app/*/*.py --check-only"
    ;;
"sort")
    echo "docker-compose exec backend /bin/sh -c \"isort app/*/*.py\""
    docker-compose exec backend /bin/sh -c "isort app/*/*.py"
    ;;
```


```
docker-compose exec backend black .
```

```
docker-compose exec backend /bin/sh -c "isort ./*/*.py"
```