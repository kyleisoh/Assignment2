const e = React.createElement;

class itemsField extends React.Component {
    constructor(props) {
        super(props);
        this.state = { numfields:1};
    }
    

    render(){        
        const field_array = [];
        for(let i = 0; i < this.state.numfields; i++){
            const editableField = e(editableFields);
            
            let field = new(editableFields);
            //field_array.push(field.renderLeft());
            field_array.push(editableField);
            //field_array.push(editableField);
        }
        const addButton = e(
            'button',
            { onClick: () => this.setState({numfields:this.state.numfields+1}) },
            'add'
        );
        const delButton = e(
            'button',
            { onClick: () => this.setState({numfields:this.state.numfields-1}) },
            'delete'
        );
        field_array.push(addButton);
        field_array.push(delButton);
        
        return e("div", null, field_array);        
    }
}


class editableFields extends React.Component {
    constructor(props) {
        super(props);
        this.state = { name: "default", price: 0, editing:true};

        this.handleNameChange = this.handleNameChange.bind(this);
        this.handlePriceChange = this.handlePriceChange.bind(this);
    }    

    handleNameChange(event) {
        this.setState({name: event.target.value});
    }

    handlePriceChange(event) {
        this.setState({price: event.target.value});
    }
  
    render() {
        let leftCol;
        let midCol;
        let rightCol;

        if(this.state.editing == true){
            const nameField = e("input", {value: this.state.name, onChange: this.handleNameChange});    
            const priceField = e("input", {value: this.state.price, onChange: this.handlePriceChange});
            const saveButton = e(
                'button',
                { onClick: () => this.setState({ editing: false }) },
                'Save'
              );
            leftCol = e("div", {class: "col-sm"}, nameField);
            midCol = e("div", {class: "col-sm"}, priceField);
            rightCol = e("div", {class: "col-sm"}, saveButton);
            //return e("body", null, nameField, " ", priceField, saveButton);
        }
        else{
            const nameLabel = e("span", null, this.state.name);
            const priceLabel = e("span", null, this.state.price);
            const editButton = e(
                'button',
                { onClick: () => this.setState({ editing: true }) },
                'Edit'
              );
            leftCol = e("div", {class: "col-sm"}, nameLabel);
            midCol = e("div", {class: "col-sm"}, priceLabel);
            rightCol = e("div", {class: "col-sm"}, editButton);
            //return e("p", null, nameLabel, priceLabel, editButton);
        }
        return e("div", {class: "row"}, leftCol, midCol, rightCol);
    }
}

const domContainer = document.querySelector('#interface');
const root = ReactDOM.createRoot(domContainer);
root.render(e(itemsField));




