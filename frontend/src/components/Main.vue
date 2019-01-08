<template>
  <div class="container">
    <button type="button" class="btn btn-primary">{{ message }}</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Main',
  data () {
    return {
      message: 'Sin mensaje'
    }
  },
  methods: {
    getMessages () {
      const path = 'http://localhost:5000/demo'
      axios.get(path).then((response) => {
        this.message = response.data
      })
      .catch((error) => {
        console.log(error)
      })
    }
  },
  created () {
    this.getMessages()
  }
}
</script>
