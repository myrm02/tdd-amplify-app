# App Amplify

This template should help get you started developing with Vue 3 in Vite.

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Customize configuration

See [Vite Configuration Reference](https://vite.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```

Pour tester l'API via l'url "" :

  - Pour récupérer les informations d'un utilisateur -> /userInfos (route API) avec comme request body : {"username": "admin@admin.com"}
  - Pour créer un utilisateur -> /createUser (route API) avec comme request body : {"email": {email}, "password": {password}}
