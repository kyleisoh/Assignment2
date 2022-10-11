const e = React.createElement;

class itemsField extends React.Component {
    constructor(props) {
        super(props);
        this.state = { numfields:1};
    }
    

    render(){        
        const field_array = [];
        const namelabel = e("div", {class: "col-sm"}, e("span", null, "Item Name"));
        const pricelabel = e("div", {class: "col-sm"}, e("span", null, "Price"));
        const amountlabel = e("div", {class: "col-sm"}, e("span", null, "Amount"));
        const placeHolder = e("div", {class: "col-sm"});
        field_array.push(e("div", {class: "row"}, namelabel, pricelabel, amountlabel, placeHolder));

        for(let i = 0; i < this.state.numfields; i++){
            const editableField = e(editableFields);                                
            field_array.push(editableField);            
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
        field_array.push(e("hr", null, null));

        
        
        return e("div", null, field_array);        
    }
}


class editableFields extends React.Component {
    constructor(props) {
        super(props);
        this.state = { name: "default", price: 0, amount: 0, editing:true};

        this.handleNameChange = this.handleNameChange.bind(this);
        this.handlePriceChange = this.handlePriceChange.bind(this);
        this.handleAmountChange = this.handleAmountChange.bind(this);
    }    

    handleNameChange(event) {
        this.setState({name: event.target.value});
    }

    handlePriceChange(event) {
        this.setState({price: event.target.value});
    }
    handleAmountChange(event){
        this.setState({amount: event.target.value});
    }
  
    render() {
        let col1;
        let col2;
        let col3;
        let col4;

        if(this.state.editing == true){
            const nameField = e("input", {value: this.state.name, onChange: this.handleNameChange, class: "form-control"});    
            const priceField = e("input", {value: this.state.price, onChange: this.handlePriceChange, class: "form-control"});
            const amountField = e("input", {value: this.state.amount, onChange: this.handleAmountChange, class: "form-control"});
            const saveButton = e(
                'button',
                { onClick: () => this.setState({ editing: false }), class:"btn btn-outline-primary"},
                'Save'
              );
            col1 = e("div", {class: "col-sm"}, nameField);
            col2 = e("div", {class: "col-sm"}, priceField);
            col3 = e("div", {class: "col-sm"}, amountField);
            col4 = e("div", {class: "col-sm"}, saveButton);
            //return e("body", null, nameField, " ", priceField, saveButton);
        }
        else{
            const nameLabel = e("span", null, this.state.name);
            const priceLabel = e("span", null, this.state.price);
            const amountLabel = e("span", null, this.state.amount);
            const editButton = e(
                'button',
                { onClick: () => this.setState({ editing: true }), class:"btn btn-outline-primary"},
                'Edit'
              );
            col1 = e("div", {class: "col-sm"}, nameLabel);
            col2 = e("div", {class: "col-sm"}, priceLabel);
            col3 = e("div", {class: "col-sm"}, amountLabel);
            col4 = e("div", {class: "col-sm"}, editButton);
            //return e("p", null, nameLabel, priceLabel, editButton);
        }
        return e("div", {class: "input"}, e("div", {class: "row"}, col1, col2, col3, col4));
    }
}

const domContainer = document.querySelector('#interface');
const root = ReactDOM.createRoot(domContainer);
root.render(e(itemsField));




