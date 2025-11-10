from fastapi import FastAPI
from routes.actividadRouter import router as actividadRouter
from routes.usuarioRouter import router as usuarioRouter
from routes.destinoRouter import router as destinoRouter

app = FastAPI()
app.include_router(actividadRouter)
app.include_router(usuarioRouter)
app.include_router(destinoRouter)