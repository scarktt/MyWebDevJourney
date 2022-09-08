const { createApp } = Vue

createApp({
  data() {
    return {
      count: 0,
      now: new Date()
    }
  },

  methods: {
    increment() {
      this.count++
    },

    decrement() {
      this.count--
    },

    sendLastValue(lastValue) {
      console.log(`Sending last value ${lastValue} to server...`)
    }
  },

  computed: {
    today() {
      return `Executed on ${this.now.toLocaleString()}` 
    }
  },

  watch: {
    count(value) {
      this.sendLastValue(value)
    }
  },

  template: `
    <section class="container">
      <p>{{ count }}</p>
      <div class="buttons">
        <button @click="decrement" class="btn-count">
          Decrement count
        </button>
        <button @click="increment" class="btn-count">
          Increment count
        </button>
      </div>
      <p class="date">{{ today }}</p>
    </section>
  `,

  mounted() {
    console.log(`The initial count is ${this.count}.`)
  }
}).mount('#app')
