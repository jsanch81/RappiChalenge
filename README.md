# Rappi Challenge

### Ejecución

Para la ejecución del proyecto, unicamente se necesita tener instalado docker y docker-compose.

En el momento de clonar el repositorio, se debe de crear en el lugar donde esta el ``docker-compose.yml`` una carpeta llamada ``mongo-volume``, en la cual se guardará los datos que se estén almacenando en el contenedor de la base de datos. Luego de esto para la ejecución, unicamente es necesario utilizar el siguiente comando.

``` docker-compose up -d --build ```

Luego de esto se puede utilizar el api generado en la siguiente url http://localhost:5000

### API

Para utiizar el API creado en la url, se tienen los siguientes paths:

PATH | METHOD | requests| response
-----|--------|---------|--------
'/api/get/prediction'| GET | {"order_id","store_id","to_user_distance","to_user_elevation","total_earning","created_at"} or \[{"order_id","store_id","to_user_distance","to_user_elevation","total_earning","created_at"}\] | {"0":{"hour","month","store_id","taken_prediction","to_user_distance","to_user_elevation","total_earning","weekday"}}
'/api/get/estimators/| GET | no required |  \[{"hour","month","store_id","taken_prediction","to_user_distance","to_user_elevation","total_earning","weekday"}\]


Con el primer api ``/api/get/prediction``, se toman envia un solo json con los datos, o una lista de json con los datos para poder realizar la predicción. Donde se está realizando la transformación de estos, y se cargan los archivos de los modelos previamente entrenados, para ser utilizados y luego proceder a realizatr la predicción. Esta predicción es almacenada en la base de datos, con las variables que se utilizarón para predeccir. Actualmente todo esto está siendo almacenado en mongodb.

Con el segundo api ``/api/get/estimators/``, se obtienen los datos almacenados en la base de datos