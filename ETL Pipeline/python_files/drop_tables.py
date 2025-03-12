from sqlalchemy import create_engine, text

# Database connection details
DATABASE_URL = "postgresql://postgres:string1@localhost:5432/hospital_operations"

def drop_all_tables():
    """Drops all tables from the PostgreSQL database using CASCADE and commits the transaction."""
    try:
        # Create a database connection
        engine = create_engine(DATABASE_URL)

        with engine.connect() as connection:
            # Fetch all tables in the public schema
            result = connection.execute(
                text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
            )
            tables = [row[0] for row in result]

            if not tables:
                print("No tables found in the database.")
            else:
                for table in tables:
                    print(f"Dropping table: {table}")
                    connection.execute(text(f"DROP TABLE IF EXISTS {table} CASCADE;"))

                # Commit the transaction
                connection.commit()

                print("All tables have been dropped successfully.")

    except Exception as e:
        print(f"Error occurred: {e}")