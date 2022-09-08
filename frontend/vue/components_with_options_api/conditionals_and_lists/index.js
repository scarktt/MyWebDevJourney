const { createApp } = Vue;

createApp({
  data() {
    return {
      label: "Para acceder ingrese su nombre de usuario. <br>No se preocupe, nosotros lo registraremos automáticamante.",
      loggedIn: false,
    }
  },
  
  watch: {
    loggedIn(value) {
      if (value) {
        this.label = "Para acceder ingrese su nombre de usuario. <br>No se preocupe, nosotros lo registraremos automáticamante."
      } else {
        this.label = "Ahora puede elegir a que universo desea viajar."
      }
    }
  },

  template: `
    <div v-if=''>
    <h1>Bienvenido a esta simulación</h2>
    <p v-html='label'></p>
    <input type="input" placeholder="nombre de usuario aquí">
    <button @click="loggedIn = !loggedIn">
      <div v-if="!loggedIn">Ingresar</div>
      <div v-if="loggedIn">Salir</div>
    </button>
  `

}).mount('#app');
