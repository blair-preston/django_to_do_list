Table todos {
  id int [pk, increment] 
  label varchar [not null]
  description varchar [note: 'optional']
  category_id int [ref: > categories.id] [not null]
  created_at timestamp [not null]
  priority_id int [ref: > priorities.id] [not null]
  duedate datetime [note: 'optional']
  status_id varcahr [ref: > status.id] [not null]
  user_id int [ref: > users.id] [not null]
}

Table categories {
  id int [pk, increment]
  title varchar [not null]
  color varchar [not null]
  user_id int [ref: > users.id] [not null]
 }

Table events {
  id int [pk, increment]
  label varchar [not null]
  description varchar [note: 'optional']
  category_id int [ref: > categories.id] [not null]
  duration duration [not null]
  location varchar [not null]
  user_id int [ref: > users.id] [not null]
}

Table daily {
  id int [pk, increment]
  label varchar [not null]
  category_id int [ref: > categories.id] [note: 'optional']
  user_id int [ref: > users.id] [not null]
}

Table priorities {
  id int [pk, increment]
  label varchar [not null]
}

Table users {
  id int [pk, increment]
  name varchar [not null]
}

Table status {
  id int [pk, increment]
  label varchar [not null]
}