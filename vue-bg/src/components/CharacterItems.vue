<template>
    <h3>{{ characterLogged }}</h3>
<table class = "infoSeason-table" v-if="!loadingCharacter">
    <thead>
          <tr>
          <th colspan="2"><h2>TEMPORADA {{ character.season }}</h2></th>
          </tr>
      </thead>
    <tbody>
      <tr>
        <th>NOM</th>
        <td>{{ character.nickname }}</td>
      </tr>
      <tr>
        <th>NIVELL</th>
        <td>{{ character.level }}</td>
      </tr>
      <tr>
        <th>EXPERIENCIA</th>
        <td>{{ character.exp }}</td>
      </tr>
      <tr>
        <th>MANÀ</th>
        <td>{{ character.mana }}</td>
      </tr>
      <tr>
        <th>VIDA</th>
        <td>{{ character.life }}</td>
      </tr>
    </tbody>
  </table>
</template>
<script>
export default {
  name: 'CharacterItems',
  data() {
    return {
      character: null,
      loadingCharacter: true,
    }
  },
  methods: {

    async getCharacterItems() {
      try {
        const response = await fetch(`/api/getCharacter/`+this.character.characterLogged.id);
        const data = await response.json();
        this.character = data.character;
        this.loadingCharacter = false;
      } catch (error) {
        console.error(error);
        this.loadingCharacter = false;
      }
    },
  },
  mounted() {
    this.character = JSON.parse(document.getElementById('infoCharacter').getAttribute('data') || '{}');
    this.getCharacterItems()
  },
}
</script>