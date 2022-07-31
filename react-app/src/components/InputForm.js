class InputForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: "",
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({ value: event.target.value });
  }

  handleSubmit(event) {
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          Year:
          <input type="number" value={this.state.value} onChange={this.handleChange} min="2014" max="2019" />
        </label>
       <label for="drugs">Choose Drug Type:</label>
       <select id="cars" name="drugs" size="3" multiple>
           <option value="M">M</option>
           <option value="N">N</option>
           <option value="R">R</option>
        </select>
        <input type="submit" value="Submit" />
      </form>
    );
  }
}
