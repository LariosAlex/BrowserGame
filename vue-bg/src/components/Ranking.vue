<template>
  <div>
    <table class='ranking-table'>
      <thead>
        <tr>
          <th>Posició</th>
          <th>Usuari</th>
          <th>Nickname</th>
          <th>Nivell</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(character, index) in characters.splice(nCharacters - charactersInPage, nCharacters)" :key="character.id">
          <td>{{ index + 1 }}</td>
          <td>{{ character.user }}</td>
          <td>{{ character.nickname }}</td>
          <td>{{ character.level }}</td>
        </tr>
      </tbody>
    </table>
  </div>
  {{ nPages() }}
</template>
<script>
import $ from 'jquery'
export default {
    name: 'RankingList',
    data() {
        const charactersInPage = 5;
        return {
            charactersInPage,
            nCharacters: charactersInPage,
            characters: [],
        }
    },
    methods: {
        getRanking() {
            $.getJSON('/api/getRanking', (data) => {
                this.characters = data.characters;
                console.log(this.characters)
            });
        },
        nPages() {
            return Math.ceil(this.characters.length /this.charactersInPage)
        },
    },
    created() {
        this.getRanking();
    },
    watch: {
        nCharacters() {
            this.getRanking()
        },
    },
}
</script>