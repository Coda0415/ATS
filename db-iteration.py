import os
import sqlite3
import re
from inflection import camelize


def clean_table_name(table_name):
    cleaned_name = re.sub(r'[\s#()&]+', '', table_name)
    return cleaned_name


def create_class(table_name, columns):
    cleaned_table_name = clean_table_name(table_name)
    class_name = camelize(cleaned_table_name)
    class_code = f"class {class_name}(db.Model):\n"
    class_code += f"    __tablename__ = '{table_name}'\n"

    has_primary_key = False
    for column in columns:
        column_name, column_type, nullable = column
        print(f"Column name: {column_name}, type: {column_type}, nullable: {nullable}")

        # Set a default type if the column_type is empty or not recognized
        if not column_type:
            column_type = "String"
            print(f"Column type not found, setting default type: {column_type}")

        if not nullable:
            has_primary_key = True
        class_code += f"    {column_name} = db.Column(db.{column_type}, nullable={nullable})\n"

    if not has_primary_key:
        # Create an auto-incrementing primary key column if none exists
        class_code += f"    id = db.Column(db.Integer, primary_key=True, autoincrement=True)\n"
        print("Added primary key column 'id'")

    class_code += "\n    def __repr__(self):\n"
    class_code += f"        return f'<{class_name} {{self.id}}>'\n\n"
    return class_code


def get_tables(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return [table[0] for table in cursor.fetchall()]


def get_columns(cursor, table_name):
    cursor.execute(f'PRAGMA table_info("{table_name}");')
    columns = []
    for column in cursor.fetchall():
        columns.append((column[1], column[2], bool(column[3])))
    return columns


def main():
    db_path = os.path.join('instance', 'frantz.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    tables = get_tables(cursor)
    models_code = "from . import db\n\n"

    for table_name in tables:
        columns = get_columns(cursor, table_name)
        class_code = create_class(table_name, columns)
        models_code += class_code

    with open('main/models.py', 'w') as f:
        f.write(models_code)

    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
