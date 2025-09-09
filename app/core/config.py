from pydantic_settings import BaseSettings


class PostgresqlSettings(BaseSettings):
    HOST: str
    USERNAME: str
    PASSWORD: str
    PORT: str

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.USERNAME}:{self.PASSWORD}@{self.HOST}:{self.PORT}/postgres"


postgresql_settings = PostgresqlSettings()
