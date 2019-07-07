//add an item
class AddPanel extends React.Component{
    render() {
        return (
            <form name="add" action="/todolist/add" method="post">
                <table>
                    <tr>
                        <td>Name:</td>
                        <td><input name="name" /></td>
                    </tr>
                    <tr>
                        <td>Content:</td>
                        <td><input name="content" /></td>
                    </tr>
                    <tr>
                        <td>Expire Date:</td>
                        <td><input type="date" name="expire_date" /></td>
                    </tr>
                    <tr>
                        <td>Priority:</td>
                        <td>
                            <select className="select" name="priority">
                                <option value="1" selected>Low</option>
                                <option value="2">High</option>
                            </select>
                        </td>
                    </tr>
                </table>
                <br/>
                <button class="button" type="submit">Add</button>
            </form>
        );
    }
};

//change the order
class OrderPanel extends React.Component{
    render() {
        return (
            <form name="order" action="/todolist/" method="post">
                <table>
                    <tr>
                        <td>
                            <select className="select" name="seq">
                                <option value="0" selected>Time Created</option>
                                <option value="1">Priority</option>
                                <option value="2">Expire Date</option>
                            </select>
                        </td>
                        <td><button className="button" type="submit">Order</button></td>
                    </tr>
                </table>
                <br/>
            </form>
        );
    }
}

//status entry
function Status(props) {
    if (props.status==0) {
        //change status
        return (
            <form name="status" action="/todolist/status" method="POST">
                <input type="hidden" name="id" value={props.id}  />
                <button class="button" type="submit">√</button>
            </form>
        );
    }
    return <div />;
};

//priority entry
function Priority(props) {
    if (props.priority==1) {
        return (
            <div>
                <label>Priority: Low</label><br />
            </div>
        );
    }
    return (
        <div>
            <label>Priority: High</label><br />
        </div>
    );
};

//include details and edit
class Item extends React.Component {
    constructor(props) {
        super(props);
        this.state = {edit: false};
    }

    handleEditClick() { this.setState({edit: true}); }
    handleCancelClick() { this.setState({edit: false}); }

    //button for switching the functions
    Button(props) {
        return (
            <button class="button" onClick={props.onClick}>
                {props.text}
            </button>
        );
    }

    //switching panels
    Switch(props) {
        if (props.edit) {
            return (
                <Edit
                    id={props.id}
                    name={props.name}
                    content={props.content}
                    expire_date={props.expire_date}
                    status={props.status}
                    priority={props.priority}
                />
            );
        }
        return (
            <Origin
                id={props.id}
                name={props.name}
                content={props.content}
                expire_date={props.expire_date}
                status={props.status}
                priority={props.priority}
            />
        );
    }

    render() {
        let button;

        if (this.state.edit) {
            button =
                <this.Button
                    onClick={this.handleCancelClick.bind(this)}
                    text="Cancel"
                />;
        }
        else {
            button =
                <this.Button
                    onClick={this.handleEditClick.bind(this)}
                    text="Edit"
                />;
        }

        return (
            <div>
                <table>
                    <tr>
                        <th>
                            {button}
                        </th>
                        <th>
                            <this.Switch
                                edit={this.state.edit}
                                id={this.props.id}
                                name={this.props.name}
                                content={this.props.content}
                                expire_date={this.props.expire_date}
                                status={this.props.status}
                                priority={this.props.priority}
                            />
                        </th>
                    </tr>
                </table>
            </div>
        );
    }
}

function Edit(props) {
    return (
        <div>
            <form name="add" action="/todolist/edit" method="post">
                <table align="left">
                    <tr>
                        <th>
                            <input type="hidden" name="id" value={props.id} />
                            Name:
                            <input name="name" value={props.name} /><br />
                            Content:
                            <input name="content" value={props.content} /><br />
                            Expire Date:
                            <input type="date" name="expire_date" value={props.expire_date} /><br />
                        </th>
                        <th>
                            Status:
                            <select class="select" name="status">
                                <option value="0" selected>Pending</option>
                                <option value="1">Complete</option>
                            </select><br />
                            Priority:
                            <select class="select" name="priority">
                                <option value="1" selected>Low</option>
                                <option value="2">High</option>
                            </select>
                        </th>
                        <th>
                            <button class="button" type="submit">Submit</button><br />
                        </th>
                    </tr>
                </table>
            </form>
        </div>
    );
}

class Origin extends React.Component {
    constructor(props) {
        super(props);
        this.state = {opacity: 1.0 - this.props.status * 0.7};
    }

    Details(props) {
        return (
            <div>
                <table align="center">
                    <tr>
                        <th>
                            <h2>{props.name}</h2>
                        </th>
                        <th>
                            <label>Expire Date: {props.expire_date}</label>
                        </th>
                        <th>
                            <Priority priority={props.priority} />
                        </th>
                    </tr>
                </table>
                <table>
                    <tr>
                        <th>
                            <label>Content: {props.content}</label>
                        </th>
                    </tr>
                </table>
            </div>
        );
    }

    render() {
        return (
            <div>
                <table>
                    <tr>
                        <th>
                            <Status status={this.props.status} id={this.props.id} />
                            <form name="delete" action="/todolist/delete" method="POST">
                                <input type="hidden" name="id" value={this.props.id} />
                                <button class="button" type="submit">×</button><br />
                            </form>
                        </th>
                        <th>
                            <div style={this.state}>
                                <this.Details
                                    name={this.props.name}
                                    content={this.props.content}
                                    expire_date={this.props.expire_date}
                                    priority={this.props.priority}
                                />
                            </div>
                        </th>
                    </tr>
                </table>
            </div>
        );
    }
}