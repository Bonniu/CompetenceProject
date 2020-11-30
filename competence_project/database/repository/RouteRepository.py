from model.route import Route


class RouteRepository:

    @staticmethod
    def insert_route(db, db_cursor, route: Route):
        query = "INSERT INTO CP_database.route (user_id, longest_route) VALUES (%s, %s)"
        db_cursor.execute(query, (route.user_id, route.longest_route))
        db.commit()
        route.id = db_cursor.lastrowid
        return route

    @staticmethod
    def insert_routes(db, db_cursor, routes: []):
        for route in routes:
            RouteRepository.insert_route(db, db_cursor, route)

    @staticmethod
    def select_routes_for_id(db_cursor, user_id) -> []:
        query = "SELECT * FROM CP_database.route"
        if user_id is not None:
            query += " WHERE user_id=" + str(user_id)
        db_cursor.execute(query)
        routes = []
        for result_route in db_cursor.fetchall():
            routes.append(RouteRepository.get_routes_from_result(result_route))
        return routes

    @staticmethod
    def get_routes_from_result(result) -> Route:
        # 0id 1user_id 2hotspot_id 3entry_time 4exit_time
        route = Route(result[1], result[2])
        return route
