-- Doc
USE hbnb_dev_db;

-- States
INSERT INTO states (id, name, created_at, updated_at) VALUES ("my_id_c", "California", CURDATE(), CURDATE());
INSERT INTO states (id, name, created_at, updated_at) VALUES ("my_id_a", "Arizona", CURDATE(), CURDATE());

-- Cities
INSERT INTO cities (id, state_id, name, created_at, updated_at) VALUES ("my_id_c_0", "my_id_c", "San Francisco", CURDATE(), CURDATE());
INSERT INTO cities (id, state_id, name, created_at, updated_at) VALUES ("my_id_c_1", "my_id_c", "San Jose", CURDATE(), CURDATE());
INSERT INTO cities (id, state_id, name, created_at, updated_at) VALUES ("my_id_a_0", "my_id_a", "Page", CURDATE(), CURDATE());
INSERT INTO cities (id, state_id, name, created_at, updated_at) VALUES ("my_id_a_1", "my_id_a", "Phoenix", CURDATE(), CURDATE());

-- Users
INSERT INTO users (id, email, password, first_name, last_name, created_at, updated_at) VALUES ("my_id_u_0", "a@a0.com", "pwd0", "fn0", "ln0", CURDATE(), CURDATE());
INSERT INTO users (id, email, password, created_at, updated_at) VALUES ("my_id_u_1", "a@a1.com", "pwd1", CURDATE(), CURDATE());
INSERT INTO users (id, email, password, created_at, updated_at) VALUES ("my_id_u_2", "a@a2.com", "pwd2", CURDATE(), CURDATE());
INSERT INTO users (id, email, password, created_at, updated_at) VALUES ("my_id_u_3", "a@a3.com", "pwd3", CURDATE(), CURDATE());

-- Places
INSERT INTO places 
(id, city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, created_at, updated_at) 
VALUES ("my_id_p_0", "my_id_c_0", "my_id_u_0", "House 0", "desc", 4, 2, 10, 100, 12.4, 14.3, CURDATE(), CURDATE());
INSERT INTO places 
(id, city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, created_at, updated_at) 
VALUES ("my_id_p_1", "my_id_c_0", "my_id_u_0", "House 1", "desc", 2, 1, 5, 50, -12.4, 0.3, CURDATE(), CURDATE());
INSERT INTO places 
(id, city_id, user_id, name, number_rooms, number_bathrooms, max_guest, price_by_night, created_at, updated_at) 
VALUES ("my_id_p_2", "my_id_c_0", "my_id_u_1", "Test House 2", 0, 0, 0, 0, CURDATE(), CURDATE());
INSERT INTO places 
(id, city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, created_at, updated_at) 
VALUES ("my_id_p_3", "my_id_c_1", "my_id_u_1", "House Bla", "desc", 4, 2, 7, 150, CURDATE(), CURDATE());

-- Amenities
INSERT INTO amenities (id, name, created_at, updated_at) VALUES ("my_id_0", "my_name_0", CURDATE(), CURDATE());
INSERT INTO amenities (id, name, created_at, updated_at) VALUES ("my_id_1", "my_name_1", CURDATE(), CURDATE());
INSERT INTO amenities (id, name, created_at, updated_at) VALUES ("my_id_2", "my_name_2", CURDATE(), CURDATE());
INSERT INTO amenities (id, name, created_at, updated_at) VALUES ("my_id_3", "my_name_3", CURDATE(), CURDATE());

-- place_amenity
INSERT INTO place_amenity (place_id, amenity_id) VALUES ("my_id_p_0", "my_id_0");
INSERT INTO place_amenity (place_id, amenity_id) VALUES ("my_id_p_0", "my_id_1");
INSERT INTO place_amenity (place_id, amenity_id) VALUES ("my_id_p_0", "my_id_2");

INSERT INTO place_amenity (place_id, amenity_id) VALUES ("my_id_p_1", "my_id_1");

INSERT INTO place_amenity (place_id, amenity_id) VALUES ("my_id_p_3", "my_id_3");
INSERT INTO place_amenity (place_id, amenity_id) VALUES ("my_id_p_3", "my_id_2");
