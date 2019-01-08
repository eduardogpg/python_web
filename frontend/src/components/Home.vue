<template>
  <div class="alert alert-primary" role="alert">
    {{message}}
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Main',
  data () {
    return {
      message: 'Home desde el Vue.js'
    }
  },
}
</script>
