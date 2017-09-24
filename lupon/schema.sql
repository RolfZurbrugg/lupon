drop table if exits users;
create table users (
	id integer primary ke autoincrement,
	username text not null,
	password text not null
);
