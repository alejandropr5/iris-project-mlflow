import mlflow

# mlflow run https://github.com/alejandropr5/iris-project-mlflow -P nsplits=20
if __name__ == '__main__':
    mlflow.projects.run(
        'https://github.com/alejandropr5/iris-project-mlflow',
        backend='local',
        parameters={
            'nsplits': 5
        })
