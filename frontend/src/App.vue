<template>
  <div class="quiz">
    <h1>Capital City Quiz</h1>

    <div v-if="country" class="question-box">
      <p class="question">What is the capital of <strong>{{ country }}</strong>?</p>
      <input v-model.trim="userAnswer" placeholder="Enter capital" :disabled="isSubmitted" />
      <button class="submit-btn" @click="submitAnswer" :disabled="isSubmitted || !userAnswer">
        Submit
      </button>
    </div>

    <div v-if="result" class="result" :class="{ incorrect: result === 'incorrect' }">
      <template v-if="result === 'correct'"> <strong>Correct!</strong></template>
      <template v-else>
        <strong>Incorrect!</strong> The correct answer is:
        <span class="correct-capital">{{ correctAnswer }}</span>
      </template>
    </div>

    <button class="next-btn" v-if="isSubmitted" @click="fetchNewQuestion">
      Next Question
    </button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CapitalQuiz',
  data() {
    return {
      country: '',
      correctAnswer: '',
      userAnswer: '',
      result: '',
      isSubmitted: false
    }
  },
  created() {
    this.fetchNewQuestion()
  },
  methods: {
    async fetchNewQuestion() {
      this.result = ''
      this.userAnswer = ''
      this.isSubmitted = false

      try {
        const res = await axios.get('http://127.0.0.1:8000/api/country/')
        this.country = res.data.country
        this.correctAnswer = res.data.correct_capital
      } catch (error) {
        console.error('Failed to fetch country:', error)
      }
    },
    async submitAnswer() {
      if (!this.userAnswer) return

      try {
        const res = await axios.post('http://127.0.0.1:8000/api/check/', {
          answer: this.userAnswer,
          actual: this.correctAnswer
        })
        this.result = res.data.result
        this.isSubmitted = true
      } catch (error) {
        console.error('Failed to submit answer:', error)
      }
    }
  }
}
</script>

<style scoped>
.quiz {
  font-family: 'Segoe UI', sans-serif;
  max-width: 600px;
  margin: 100px auto;
  text-align: center;
  padding: 30px;
  border: 2px solid #ddd;
  border-radius: 16px;
  background-color: #fdfdfd;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

h1 {
  color: #34495e;
  margin-bottom: 30px;
}

.question-box {
  margin-bottom: 20px;
}

.question {
  font-size: 18px;
  margin-bottom: 15px;
  color: #2c3e50;
}

input {
  padding: 10px;
  font-size: 16px;
  width: 60%;
  border-radius: 6px;
  border: 1px solid #ccc;
  margin-bottom: 10px;
}

.submit-btn,
.next-btn {
  background-color: #3498db;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s;
  font-size: 16px;
  margin-top: 10px;
}

.submit-btn:hover,
.next-btn:hover {
  background-color: #2980b9;
}

.submit-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.result {
  font-size: 18px;
  margin-top: 20px;
  color: green;
}

.result.incorrect {
  color: red;
}

.correct-capital {
  font-weight: bold;
  color: #34495e;
}
</style>
