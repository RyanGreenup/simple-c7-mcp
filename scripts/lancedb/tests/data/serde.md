### Implement Serialize for i32 Primitive in Rust

Source: https://serde.rs/impl-serialize

An example of implementing the `Serialize` trait for the primitive `i32` type. This demonstrates how to use the `serialize_i32` method of the `Serializer`.

```Rust
impl Serialize for i32 {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: Serializer,
    {
        serializer.serialize_i32(*self)
    }
}

```

--------------------------------

### Serialize Map Start to JSON Object (Rust)

Source: https://serde.rs/impl-serializer

Shows the serialization of the beginning of a map into a JSON opening brace '{'. This is called before any key-value pairs are serialized.

```Rust
    // Maps are represented in JSON as `{ K: V, K: V, ... }`.
    fn serialize_map(self, _len: Option<usize>) -> Result<Self::SerializeMap> {
        self.output += "{";
        Ok(self)
    }
```

--------------------------------

### Rust: Implementing Deserialize for i32

Source: https://serde.rs/impl-deserialize

Example of implementing the `Deserialize` trait for the `i32` type. This implementation delegates the deserialization process to the `Deserializer` by calling `deserialize_i32` and passing an `I32Visitor`.

```rust
impl<'de> Deserialize<'de> for i32 {
    fn deserialize<D>(deserializer: D) -> Result<i32, D::Error>
    where
        D: Deserializer<'de>,
    {
        deserializer.deserialize_i32(I32Visitor)
    }
}

```

--------------------------------

### Serialize Sequence Start to JSON Array (Rust)

Source: https://serde.rs/impl-serializer

Details the serialization of the beginning of a sequence into a JSON opening bracket '['. This method is called before any sequence elements are serialized.

```Rust
    // The start of the sequence, each value, and the end are three separate
    // method calls. This one is responsible only for serializing the start, 
    // which in JSON is `[`.
    //
    // The length of the sequence may or may not be known ahead of time. This
    // doesn't make a difference in JSON because the length is not represented
    // explicitly in the serialized form. Some serializers may only be able to
    // support sequences for which the length is known up front.
    fn serialize_seq(self, _len: Option<usize>) -> Result<Self::SerializeSeq> {
        self.output += "[";
        Ok(self)
    }
```

--------------------------------

### Transcode JSON to Compacted JSON (Rust)

Source: https://serde.rs/transcode

This example demonstrates transcoding a JSON input with excess whitespace into a compacted JSON output using the serde-transcode crate and serde_json. It operates in a streaming fashion, making it memory-efficient. The core functionality relies on a Serde Deserializer and a Serde Serializer.

```rust
use std::io;

fn main() {
    // A JSON input with plenty of whitespace.
    let input = r#"#
      {
        "a boolean": true,
        "an array": [3, 2, 1]
      }
    "#;

    // A JSON deserializer. You can use any Serde Deserializer here.
    let mut deserializer = serde_json::Deserializer::from_str(input);

    // A compacted JSON serializer. You can use any Serde Serializer here.
    let mut serializer = serde_json::Serializer::new(io::stdout());

    // Prints `{"a boolean":true,"an array":[3,2,1]}` to stdout.
    // This line works with any self-describing Deserializer and any Serializer.
    serde_transcode::transcode(&mut deserializer, &mut serializer).unwrap();
}

```

--------------------------------

### Rust: Visitor Trait for Deserializing i32

Source: https://serde.rs/impl-deserialize

An implementation of the `Visitor` trait for deserializing an `i32`. This example shows how to handle different integer input types and convert them to `i32`, including range checking for `i64`.

```rust
use std::fmt;

use serde::de::{self, Visitor};

struct I32Visitor;

impl<'de> Visitor<'de> for I32Visitor {
    type Value = i32;

    fn expecting(&self, formatter: &mut fmt::Formatter) -> fmt::Result {
        formatter.write_str("an integer between -2^31 and 2^31")
    }

    fn visit_i8<E>(self, value: i8) -> Result<Self::Value, E>
    where
        E: de::Error,
    {
        Ok(i32::from(value))
    }

    fn visit_i32<E>(self, value: i32) -> Result<Self::Value, E>
    where
        E: de::Error,
    {
        Ok(value)
    }

    fn visit_i64<E>(self, value: i64) -> Result<Self::Value, E>
    where
        E: de::Error,
    {
        use std::i32;
        if value >= i64::from(i32::MIN) && value <= i64::from(i32::MAX) {
            Ok(value as i32)
        } else {
            Err(E::custom(format!("i32 out of range: {}\n", value)))
        }
    }
}

```

--------------------------------

### Implement Serialize for Color Struct in Rust

Source: https://serde.rs/impl-serialize

An example of implementing `Serialize` for an ordinary struct named `Color`. It uses the `serialize_struct` method, followed by `serialize_field` for each field, and finally `end`.

```Rust
use serde::ser::{Serialize, Serializer, SerializeStruct};

struct Color {
    r: u8,
    g: u8,
    b: u8,
}

impl Serialize for Color {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: Serializer,
    {
        let mut state = serializer.serialize_struct("Color", 3)?;
        state.serialize_field("r", &self.r)?;
        state.serialize_field("g", &self.g)?;
        state.serialize_field("b", &self.b)?;
        state.end()
    }
}

```

--------------------------------

### Rust: Basic JSON Deserializer Implementation with Serde

Source: https://serde.rs/impl-deserializer

Implements a `Deserializer` struct and related functions for parsing JSON strings into Rust types using Serde. It includes methods for peeking and consuming characters, parsing booleans, and parsing unsigned integers. The implementation is a simplified example for documentation purposes.

```Rust
use std::ops::{AddAssign, MulAssign, Neg};

use serde::Deserialize;
use serde::de::{ 
    self, DeserializeSeed, EnumAccess, IntoDeserializer, MapAccess, SeqAccess,
    VariantAccess, Visitor,
};

use error::{Error, Result};

pub struct Deserializer<'de> {
    // This string starts with the input data and characters are truncated off
    // the beginning as data is parsed.
    input: &'de str,
}

impl<'de> Deserializer<'de> {
    // By convention, `Deserializer` constructors are named like `from_xyz`.
    // That way basic use cases are satisfied by something like
    // `serde_json::from_str(...)` while advanced use cases that require a
    // deserializer can make one with `serde_json::Deserializer::from_str(...)`.
    pub fn from_str(input: &'de str) -> Self {
        Deserializer { input }
    }
}

// By convention, the public API of a Serde deserializer is one or more
// `from_xyz` methods such as `from_str`, `from_bytes`, or `from_reader`
// depending on what Rust types the deserializer is able to consume as input.
//
// This basic deserializer supports only `from_str`.
pub fn from_str<'a, T>(s: &'a str) -> Result<T>
where
    T: Deserialize<'a>,
{
    let mut deserializer = Deserializer::from_str(s);
    let t = T::deserialize(&mut deserializer)?;
    if deserializer.input.is_empty() {
        Ok(t)
    } else {
        Err(Error::TrailingCharacters)
    }
}

// SERDE IS NOT A PARSING LIBRARY. This impl block defines a few basic parsing
// functions from scratch. More complicated formats may wish to use a dedicated
// parsing library to help implement their Serde deserializer.
impl<'de> Deserializer<'de> {
    // Look at the first character in the input without consuming it.
    fn peek_char(&mut self) -> Result<char> {
        self.input.chars().next().ok_or(Error::Eof)
    }

    // Consume the first character in the input.
    fn next_char(&mut self) -> Result<char> {
        let ch = self.peek_char()?;
        self.input = &self.input[ch.len_utf8()..];
        Ok(ch)
    }

    // Parse the JSON identifier `true` or `false`.
    fn parse_bool(&mut self) -> Result<bool> {
        if self.input.starts_with("true") {
            self.input = &self.input["true".len()..];
            Ok(true)
        } else if self.input.starts_with("false") {
            self.input = &self.input["false".len()..];
            Ok(false)
        } else {
            Err(Error::ExpectedBoolean)
        }
    }

    // Parse a group of decimal digits as an unsigned integer of type T.
    //
    // This implementation is a bit too lenient, for example `001` is not
    // allowed in JSON. Also the various arithmetic operations can overflow and
    // panic or return bogus data. But it is good enough for example code!
    fn parse_unsigned<T>(&mut self) -> Result<T>
    where
        T: AddAssign<T> + MulAssign<T> + From<u8>,
    {
        let mut int = match self.next_char()? {
            ch @ '0'..='9' => T::from(ch as u8 - b'0'),
            _ => {
                return Err(Error::ExpectedInteger);
            }
        };
        loop {
            match self.input.chars().next() {
                Some(ch @ '0'..='9') => {
                    self.input = &self.input[1..];
                    int *= T::from(10);
                    int += T::from(ch as u8 - b'0');
                }
                _ => {
                    return Ok(int);
                }
            }
        }
    }

    // Parse a possible minus sign followed by a group of decimal digits as a
    // signed integer of type T.
    fn parse_signed<T>(&mut self) -> Result<T>
    where
        T: Neg<Output = T> + AddAssign<T> + MulAssign<T> + From<i8>,
    {

```

--------------------------------

### Deserialize Option Types in Rust

Source: https://serde.rs/impl-deserializer

Deserializes optional values. It checks if the input starts with 'null' to represent `None`, otherwise it assumes a present value and delegates to the visitor's `visit_some` method. This can be a lossy representation, as `Some(())` and `None` both serialize to `null`.

```rust
fn deserialize_option<V>(self, visitor: V) -> Result<V::Value>
    where
        V: Visitor<'de>,
    {
        if self.input.starts_with("null") {
            self.input = &self.input["null".len()..];
            visitor.visit_none()
        } else {
            visitor.visit_some(self)
        }
    }
```

--------------------------------

### Rust Externally Tagged Enum Example

Source: https://serde.rs/enum-representations

Demonstrates the default externally tagged enum representation in Serde. The variant name is used as a key in the serialized output. This representation is compatible with no-alloc projects and works with all variant types.

```rust
#[derive(Serialize, Deserialize)]
enum Message {
    Request { id: String, method: String, params: Params },
    Response { id: String, result: Value },
}

// JSON Output: {"Request": {"id": "...", "method": "...", "params": {...}}}

```

--------------------------------

### User Struct with Borrowed Lifetimes

Source: https://serde.rs/lifetimes

An example of a `User` struct that derives `Deserialize` and uses borrowed string slices ('a). This demonstrates how Serde can deserialize into data structures that borrow directly from the input, enabling zero-copy deserialization.

```rust
#[derive(Deserialize)]
struct User<'a> {
    id: u32,
    name: &'a str,
    screen_name: &'a str,
    location: &'a str,
}

```

--------------------------------

### Deserialize Nth Element of Sequence with IgnoredAny - Rust

Source: https://serde.rs/ignored-any

This Rust code defines `NthElement`, a struct that deserializes the nth element of a sequence while efficiently discarding all other elements using `IgnoredAny`. It requires the `serde` and `serde_json` crates. The `main` function provides an example of its usage.

```rust
use std::fmt;
use std::marker::PhantomData;

use serde::de::{
    self, Deserialize, DeserializeSeed, Deserializer, Visitor, SeqAccess,
    IgnoredAny,
};
use serde_json::json;

// A seed that can be used to deserialize only the `n`th element of a sequence
// while efficiently discarding elements of any type before or after index `n`.
//
// For example to deserialize only the element at index 3:
//
//    NthElement::new(3).deserialize(deserializer)
pub struct NthElement<T> {
    n: usize,
    marker: PhantomData<fn() -> T>,
}

impl<T> NthElement<T> {
    pub fn new(n: usize) -> Self {
        NthElement {
            n: n,
            marker: PhantomData,
        }
    }
}

impl<'de, T>
    Visitor<'de>
    for NthElement<T>
where
    T: Deserialize<'de>,
{
    type Value = T;

    fn expecting(&self, formatter: &mut fmt::Formatter) -> fmt::Result {
        write!(formatter, "a sequence in which we care about element {}", self.n)
    }

    fn visit_seq<V>(self, mut seq: V) -> Result<Self::Value, V::Error>
    where
        V: SeqAccess<'de>,
    {
        // Skip over the first `n` elements.
        for i in 0..self.n {
            // It is an error if the sequence ends before we get to element `n`.
            if seq.next_element::<IgnoredAny>()?.is_none() {
                return Err(de::Error::invalid_length(i, &self));
            }
        }

        // Deserialize the one we care about.
        let nth = seq.next_element()?
                     .ok_or_else(|| de::Error::invalid_length(self.n, &self))?;

        // Skip over any remaining elements in the sequence after `n`.
        while let Some(IgnoredAny) = seq.next_element()? {
            // ignore
        }

        Ok(nth)
    }
}

impl<'de, T>
    DeserializeSeed<'de>
    for NthElement<T>
where
    T: Deserialize<'de>,
{
    type Value = T;

    fn deserialize<D>(self, deserializer: D) -> Result<Self::Value, D::Error>
    where
        D: Deserializer<'de>,
    {
        deserializer.deserialize_seq(self)
    }
}

fn main() {
    let array = json!(["a", "b", "c", "d", "e"]);

    let nth: String = NthElement::new(3).deserialize(&array).unwrap();

    println!("{}", nth);
    assert_eq!(nth, array[3]);
}

```

--------------------------------

### Rust Serde Default Values from Function, Default Trait, and Method

Source: https://serde.rs/attr-default

This Rust code snippet demonstrates how to use `serde(default)` to specify fallback values for fields during JSON deserialization. It covers using a function (`default_resource`), the `std::default::Default` trait implementation (`Timeout`), and a method (`Priority::lowest`) as default sources. The `Request` struct is deserialized from a JSON string, showcasing how missing fields are populated with their respective defaults.

```rust
use serde::Deserialize;

#[derive(Deserialize, Debug)]
struct Request {
    // Use the result of a function as the default if "resource" is
    // not included in the input.
    #[serde(default = "default_resource")]
    resource: String,

    // Use the type's implementation of std::default::Default if
    // "timeout" is not included in the input.
    #[serde(default)]
    timeout: Timeout,

    // Use a method from the type as the default if "priority" is not
    // included in the input. This may also be a trait method.
    #[serde(default = "Priority::lowest")]
    priority: Priority,
}

fn default_resource() -> String {
    "/".to_string()
}

/// Timeout in seconds.
#[derive(Deserialize, Debug)]
struct Timeout(u32);
impl Default for Timeout {
    fn default() -> Self {
        Timeout(30)
    }
}

#[derive(Deserialize, Debug)]
enum Priority { ExtraHigh, High, Normal, Low, ExtraLow }
impl Priority {
    fn lowest() -> Self { Priority::ExtraLow }
}

fn main() {
    let json = r#"[
      {
        "resource": "/users"
      },
      {
        "timeout": 5,
        "priority": "High"
      }
    ]"#;

    let requests: Vec<Request> = serde_json::from_str(json).unwrap();

    // The first request has resource="/users", timeout=30, priority=ExtraLow
    println!("{:?}", requests[0]);

    // The second request has resource="/", timeout=5, priority=High
    println!("{:?}", requests[1]);
}

```

--------------------------------

### Rust: Skip Serializing Fields with Serde

Source: https://serde.rs/attr-skip-serializing

Demonstrates how to use `#[serde(skip_serializing)]` to prevent a field from being included in the serialized output. It also highlights the difference between `skip_serializing` and `skip` for both serialization and deserialization. The example serializes a vector of structs to JSON.

```Rust
use serde::Serialize;

use std::collections::BTreeMap as Map;

#[derive(Serialize)]
struct Resource {
    // Always serialized.
    name: String,

    // Never serialized.
    #[serde(skip_serializing)]
    hash: String,

    // Use a method to decide whether the field should be skipped.
    #[serde(skip_serializing_if = "Map::is_empty")]
    metadata: Map<String, String>,
}

fn main() {
    let resources = vec![
        Resource {
            name: "Stack Overflow".to_string(),
            hash: "b6469c3f31653d281bbbfa6f94d60fea130abe38".to_string(),
            metadata: Map::new(),
        },
        Resource {
            name: "GitHub".to_string(),
            hash: "5cb7a0c47e53854cd00e1a968de5abce1c124601".to_string(),
            metadata: {
                let mut metadata = Map::new();
                metadata.insert("headquarters".to_string(),
                                "San Francisco".to_string());
                metadata
            },
        },
    ];

    let json = serde_json::to_string_pretty(&resources).unwrap();

    // Prints:
    //
    //    [
    //      {
    //        "name": "Stack Overflow"
    //      },
    //      {
    //        "name": "GitHub",
    //        "metadata": {
    //          "headquarters": "San Francisco"
    //        }
    //      }
    //    ]
    println!("{}", json);
}

```

--------------------------------

### Rust Untagged Enum Example

Source: https://serde.rs/enum-representations

Demonstrates the untagged enum representation using `#[serde(untagged)]`. No explicit tag is used; Serde attempts to deserialize against variants in order. This requires the 'alloc' feature and supports all variant types.

```rust
#[derive(Serialize, Deserialize)]
#[serde(untagged)]
enum Message {
    Request { id: String, method: String, params: Params },
    Response { id: String, result: Value },
}

// JSON Output: {"id": "...", "method": "...", "params": {...}}

```

```rust
#[derive(Serialize, Deserialize)]
#[serde(untagged)]
enum Data {
    Integer(u64),
    Pair(String, String),
}

// Can be deserialized from an integer or an array of two strings.

```

--------------------------------

### Rust Internally Tagged Enum Example

Source: https://serde.rs/enum-representations

Illustrates the internally tagged enum representation using `#[serde(tag = "type")]`. The tag indicating the variant is embedded within the serialized data. This requires the 'alloc' feature and does not support tuple variants.

```rust
#[derive(Serialize, Deserialize)]
#[serde(tag = "type")]
enum Message {
    Request { id: String, method: String, params: Params },
    Response { id: String, result: Value },
}

// JSON Output: {"type": "Request", "id": "...", "method": "...", "params": {...}}

```

--------------------------------

### Rust Adjacently Tagged Enum Example

Source: https://serde.rs/enum-representations

Shows the adjacently tagged enum representation with `#[serde(tag = "t", content = "c")]`. The tag and content are separate fields within the same object. This requires the 'alloc' feature.

```rust
#[derive(Serialize, Deserialize)]
#[serde(tag = "t", content = "c")]
enum Block {
    Para(Vec<Inline>),
    Str(String),
}

// JSON Output:
// {"t": "Para", "c": [{...}, {...}]}
// {"t": "Str", "c": "the string"}

```

--------------------------------

### Derive Serialize/Deserialize for Remote Struct with Private Fields

Source: https://serde.rs/remote-derive

This example shows how to derive `Serialize` and `Deserialize` for a remote struct with private fields. It requires defining getters for each private field using `#[serde(getter = "...")]` within the remote definition struct. Additionally, an `impl From<RemoteDef> for RemoteType` is needed to construct the original type from the definition.

```rust
mod other_crate {
    pub struct Duration {
        secs: i64,
        nanos: i32,
    }

    impl Duration {
        pub fn new(secs: i64, nanos: i32) -> Self {
            Duration { secs: secs, nanos: nanos }
        }

        pub fn seconds(&self) -> i64 {
            self.secs
        }

        pub fn subsec_nanos(&self) -> i32 {
            self.nanos
        }
    }
}

use other_crate::Duration;
use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize)]
#[serde(remote = "Duration")]
struct DurationDef {
    #[serde(getter = "Duration::seconds")]
    secs: i64,
    #[serde(getter = "Duration::subsec_nanos")]
    nanos: i32,
}

impl From<DurationDef> for Duration {
    fn from(def: DurationDef) -> Duration {
        Duration::new(def.secs, def.nanos)
    }
}

#[derive(Serialize, Deserialize)]
struct Process {
    command_line: String,

    #[serde(with = "DurationDef")]
    wall_time: Duration,
}
```

--------------------------------

### Deserializer<'de> Lifetime with Unconstrained Lifetime in Rust

Source: https://serde.rs/lifetimes

An example of a Deserializer that does not borrow data, resulting in an unconstrained 'de lifetime parameter. This is useful when the deserializer only reads owned data.

```rust
use std::io;

struct MyDeserializer<R> {
    read: R,
}

impl<'de, R> Deserializer<'de> for MyDeserializer<R>
where
    R: io::Read,
{
    /* ... */
}

```

--------------------------------

### Rust: Serialize/Deserialize Nested JSON String with Serde

Source: https://serde.rs/convert-error

This Rust code snippet demonstrates how to use Serde to serialize and deserialize a nested structure where a field is represented as a JSON string. It defines structs for a resource and a policy, and uses a custom Serde module `as_json_string` to handle the serialization and deserialization of the policy as a JSON string. The example includes a `main` function that serializes a `Resource` object to YAML.

```Rust
use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize)]
struct Resource {
    name: String,

    #[serde(with = "as_json_string")]
    policy: Policy,
}

#[derive(Serialize, Deserialize)]
struct Policy {
    effect: String,
    action: String,
    resource: String,
}

// Serialize and deserialize logic for dealing with nested values represented as
// JSON strings.
mod as_json_string {
    use serde_json;
    use serde::ser::{Serialize, Serializer};
    use serde::de::{Deserialize, DeserializeOwned, Deserializer};

    // Serialize to a JSON string, then serialize the string to the output
    // format.
    pub fn serialize<T, S>(value: &T, serializer: S) -> Result<S::Ok, S::Error>
    where
        T: Serialize,
        S: Serializer,
    {
        use serde::ser::Error;
        let j = serde_json::to_string(value).map_err(Error::custom)?;
        j.serialize(serializer)
    }

    // Deserialize a string from the input format, then deserialize the content
    // of that string as JSON.
    pub fn deserialize<'de, T, D>(deserializer: D) -> Result<T, D::Error>
    where
        T: DeserializeOwned,
        D: Deserializer<'de>,
    {
        use serde::de::Error;
        let j = String::deserialize(deserializer)?;
        serde_json::from_str(&j).map_err(Error::custom)
    }
}

fn main() {
    let resource = Resource {
        name: "test_policy".to_owned(),
        policy: Policy {
            effect: "Allow".to_owned(),
            action: "s3:ListBucket".to_owned(),
            resource: "arn:aws:s3:::example_bucket".to_owned(),
        },
    };

    let y = serde_yaml::to_string(&resource).unwrap();
    println!("{}", y);
}

```

--------------------------------

### Implement Serialize for MyMap<K, V> Map in Rust

Source: https://serde.rs/impl-serialize

Shows how to implement `Serialize` for a map-like structure (`MyMap`). It follows a three-step process: initialize the map, serialize key-value entries, and end the map.

```Rust
use serde::ser::{Serialize, Serializer, SerializeMap};

impl<K, V> Serialize for MyMap<K, V>
where
    K: Serialize,
    V: Serialize,
{
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: Serializer,
    {
        let mut map = serializer.serialize_map(Some(self.len()))?;
        for (k, v) in self {
            map.serialize_entry(k, v)?;
        }
        map.end()
    }
}

```

--------------------------------

### Implement Serialize for Vec<T> Sequence in Rust

Source: https://serde.rs/impl-serialize

Demonstrates implementing `Serialize` for a `Vec<T>` (a sequence). It uses a three-step process: initialize the sequence, serialize each element, and end the sequence.

```Rust
use serde::ser::{Serialize, Serializer, SerializeSeq};

impl<T> Serialize for Vec<T>
where
    T: Serialize,
{
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: Serializer,
    {
        let mut seq = serializer.serialize_seq(Some(self.len()))?;
        for e in self {
            seq.serialize_element(e)?;
        }
        seq.end()
    }
}

```

--------------------------------

### Rust Unit Testing Serde with Tokens

Source: https://serde.rs/unit-testing

This snippet demonstrates how to use the `serde_test` crate to write unit tests for Serde `Serialize` and `Deserialize` implementations. It utilizes `Token` assertions to verify the sequence of serializer calls during serialization and deserialization. The `assert_tokens` function checks both directions.

```rust
use linked_hash_map::LinkedHashMap;
use serde_test::{Token, assert_tokens};

#[test]
fn test_ser_de_empty() {
    let map = LinkedHashMap::<char, u32>::new();

    assert_tokens(&map, &[
        Token::Map { len: Some(0) },
        Token::MapEnd,
    ]);
}

#[test]
fn test_ser_de() {
    let mut map = LinkedHashMap::new();
    map.insert('b', 20);
    map.insert('a', 10);
    map.insert('c', 30);

    assert_tokens(&map, &[
        Token::Map { len: Some(3) },
        Token::Char('b'),
        Token::I32(20),

        Token::Char('a'),
        Token::I32(10),

        Token::Char('c'),
        Token::I32(30),
        Token::MapEnd,
    ]);
}
```

--------------------------------

### Rust Struct Serialization/Deserialization with Serde Derive

Source: https://serde.rs/index

Demonstrates how to use Serde's derive macros (`Serialize`, `Deserialize`) to automatically generate serialization and deserialization logic for custom Rust structs. It shows conversion to and from a JSON string using the `serde_json` crate. Requires the `serde` and `serde_json` crates.

```rust
use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize, Debug)]
struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let point = Point { x: 1, y: 2 };

    // Convert the Point to a JSON string.
    let serialized = serde_json::to_string(&point).unwrap();

    // Prints serialized = {"x":1,"y":2}
    println!("serialized = {}", serialized);

    // Convert the JSON string back to a Point.
    let deserialized: Point = serde_json::from_str(&serialized).unwrap();

    // Prints deserialized = Point { x: 1, y: 2 }
    println!("deserialized = {:?}", deserialized);
}
```

--------------------------------

### Rust code using Serde derive for serialization and deserialization

Source: https://serde.rs/derive

This Rust code demonstrates how to use Serde's `derive` macro to automatically implement `Serialize` and `Deserialize` for a `Point` struct. It includes serialization to a JSON string using `serde_json` and deserialization back into the `Point` struct. Requires Rust compiler version 1.31 or newer.

```rust
use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize, Debug)]
struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let point = Point { x: 1, y: 2 };

    let serialized = serde_json::to_string(&point).unwrap();
    println!("serialized = {}", serialized);

    let deserialized: Point = serde_json::from_str(&serialized).unwrap();
    println!("deserialized = {:?}", deserialized);
}

```

--------------------------------

### Add Serde derive dependency to Cargo.toml

Source: https://serde.rs/derive

This snippet shows how to add the Serde library with the 'derive' feature enabled to your project's Cargo.toml file. This is a prerequisite for using Serde's automatic derive macros. Ensure compatible versions of other Serde-based dependencies are also used.

```toml
[package]
name = "my-crate"
version = "0.1.0"
authors = ["Me <user@rust-lang.org>"]

[dependencies]
serde = { version = "1.0", features = ["derive"] }

# serde_json is just for the example, not required in general
serde_json = "1.0"

```

--------------------------------

### Enable Serde Derive Macro in Cargo.toml for No-std

Source: https://serde.rs/no-std

To use Serde's `#[derive(Serialize, Deserialize)]` macros in a no_std crate, ensure the 'derive' feature is enabled in your Cargo.toml while keeping the default 'std' feature disabled.

```toml
[dependencies]
serde = { version = "1.0", default-features = false, features = ["derive"] }

```

--------------------------------

### Rust: CommaSeparated for SeqAccess

Source: https://serde.rs/impl-deserializer

Implements `SeqAccess` for comma-separated data, managing the state of whether an element is the first or subsequent to handle commas correctly.

```rust
impl<'de, 'a> SeqAccess<'de> for CommaSeparated<'a, 'de> {
    type Error = Error;

    fn next_element_seed<T>(&mut self, seed: T) -> Result<Option<T::Value>>
    where
        T: DeserializeSeed<'de>,
    {
        // Check if there are no more elements.
        if self.de.peek_char()? == ']' {
            return Ok(None);
        }
        // Comma is required before every element except the first.
        if !self.first && self.de.next_char()? != ',' {
            return Err(Error::ExpectedArrayComma);
        }
        self.first = false;
        // Deserialize an array element.
        seed.deserialize(&mut *self.de).map(Some)
    }
}
```

--------------------------------

### Serde Enum Mapping for OsString (Conceptual)

Source: https://serde.rs/data-model

This conceptual Rust code snippet illustrates how `std::ffi::OsString` could be represented as a Serde enum. This approach allows for platform-agnostic serialization and deserialization by explicitly handling different platform representations (Unix and Windows) as variants of an enum.

```rust
enum OsString {
    Unix(Vec<u8>),
    Windows(Vec<u16>)
    // potentially other platforms
}

```

--------------------------------

### Rust: Serialize Struct and Struct Variant with Serde

Source: https://serde.rs/impl-serializer

Implements `serialize_struct` and `serialize_struct_variant` for Serde's `Serializer`. `serialize_struct` delegates to `serialize_map`, while `serialize_struct_variant` handles externally tagged struct variants by outputting JSON in the format `{ NAME: { K: V, ... } }`.

```rust
    // looking at the serialized data.
    fn serialize_struct(
        self,
        _name: &'static str,
        len: usize,
    ) -> Result<Self::SerializeStruct> {
        self.serialize_map(Some(len))
    }

    // Struct variants are represented in JSON as `{ NAME: { K: V, ... } }`.
    // This is the externally tagged representation.
    fn serialize_struct_variant(
        self,
        _name: &'static str,
        _variant_index: u32,
        variant: &'static str,
        _len: usize,
    ) -> Result<Self::SerializeStructVariant> {
        self.output += "{";
        variant.serialize(&mut *self)?;
        self.output += ":{";
        Ok(self)
    }
}
```

--------------------------------

### Serde Struct Flattening: Factor out common pagination metadata

Source: https://serde.rs/attr-flatten

Demonstrates how to use `#[serde(flatten)]` to inline fields from a `Pagination` struct into a `Users` struct. This is useful for common metadata shared across different API responses, reducing boilerplate.

```rust
use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize)]
struct Pagination {
    limit: u64,
    offset: u64,
    total: u64,
}

#[derive(Serialize, Deserialize)]
struct Users {
    users: Vec<User>,

    #[serde(flatten)]
    pagination: Pagination,
}

// Assuming User struct is defined elsewhere
```

--------------------------------

### Serialize Tuple Struct to JSON Array (Rust)

Source: https://serde.rs/impl-serializer

Illustrates the serialization of tuple structs into JSON arrays. This method also leverages the `serialize_seq` functionality.

```Rust
    // Tuple structs look just like sequences in JSON.
    fn serialize_tuple_struct(
        self,
        _name: &'static str,
        len: usize,
    ) -> Result<Self::SerializeTupleStruct> {
        self.serialize_seq(Some(len))
    }
```

--------------------------------

### Serialize Unit to JSON Null (Rust)

Source: https://serde.rs/impl-serializer

Shows how to serialize a unit type, representing an anonymous value with no data, into JSON 'null'. This is a fundamental serialization mapping.

```Rust
    // In Serde, unit means an anonymous value containing no data. Map this to
    // JSON as `null`.
    fn serialize_unit(self) -> Result<()> {
        self.output += "null";
        Ok(())
    }
```

--------------------------------

### Rust: Borrow Attribute for Zero-Copy Deserialization

Source: https://serde.rs/variant-attrs

Explains `#[serde(borrow)]` and `#[serde(borrow = "'a + 'b + ...")]` for enabling zero-copy deserialization on newtype variants.

```rust
#[derive(Serialize, Deserialize)]
enum Data {
    #[serde(borrow)]
    VariantName(String),
}

#[derive(Serialize, Deserialize)]
enum DataWithLifetimes {
    #[serde(borrow = "'a")]
    VariantName<'a>( &'a str ),
}

```

--------------------------------

### Serialize Tuple to JSON Array (Rust)

Source: https://serde.rs/impl-serializer

Shows how tuples are serialized into JSON arrays, similar to sequences. The length is known and can be passed to the `serialize_seq` method.

```Rust
    // Tuples look just like sequences in JSON. Some formats may be able to
    // represent tuples more efficiently by omitting the length, since tuple
    // means that the corresponding `Deserialize implementation will know the
    // length without needing to look at the serialized data.
    fn serialize_tuple(self, len: usize) -> Result<Self::SerializeTuple> {
        self.serialize_seq(Some(len))
    }
```

--------------------------------

### Basic Serde Data Format Crate Structure (Rust)

Source: https://serde.rs/conventions

This snippet demonstrates the fundamental structure of a Serde data format crate's root module. It declares internal modules for deserialization, error handling, and serialization, and then re-exports key types and functions for public use, adhering to Serde conventions.

```rust
mod de;
mod error;
mod ser;

pub use de::{from_str, Deserializer};
pub use error::{Error, Result};
pub use ser::{to_string, Serializer};

```

--------------------------------

### Rust: Serialize Map with Serde

Source: https://serde.rs/impl-serializer

Implements Serde's `SerializeMap` trait for JSON output. It serializes map keys and values, prepending a comma if it's not the first entry in the map. It assumes keys serialize to strings, as required by JSON, and places a colon `:` between keys and values. The map is enclosed in curly braces `{}`.

```rust
// Some `Serialize` types are not able to hold a key and value in memory at the same time so `SerializeMap` implementations are required to support `serialize_key` and `serialize_value` individually.
//
// There is a third optional method on the `SerializeMap` trait. The
// `serialize_entry` method allows serializers to optimize for the case where
// key and value are both available simultaneously. In JSON it doesn't make a
// difference so the default behavior for `serialize_entry` is fine.
implement<'a> ser::SerializeMap for &'a mut Serializer {
    type Ok = ();
    type Error = Error;

    // The Serde data model allows map keys to be any serializable type. JSON
    // only allows string keys so the implementation below will produce invalid
    // JSON if the key serializes as something other than a string.
    //
    // A real JSON serializer would need to validate that map keys are strings.
    // This can be done by using a different Serializer to serialize the key
    // (instead of `&mut **self`) and having that other serializer only
    // implement `serialize_str` and return an error on any other data type.
    fn serialize_key<T>(&mut self, key: &T) -> Result<()> 
    where
        T: ?Sized + Serialize,
    {
        if !self.output.ends_with('{') {
            self.output += ",";
        }
        key.serialize(&mut **self)
    }

    // It doesn't make a difference whether the colon is printed at the end of
    // `serialize_key` or at the beginning of `serialize_value`. In this case
    // the code is a bit simpler having it here.
    fn serialize_value<T>(&mut self, value: &T) -> Result<()> 
    where
        T: ?Sized + Serialize,
    {
        self.output += ":";
        value.serialize(&mut **self)
    }
}
```

--------------------------------

### Rust: Combined Custom Serialization and Deserialization

Source: https://serde.rs/variant-attrs

Illustrates `#[serde(with = "module")]` for using separate `serialize` and `deserialize` functions from a specified module.

```rust
mod custom_module {
    use serde::{Serialize, Serializer, Deserialize, Deserializer};
    pub fn serialize<S>(data: &MyData, s: S) -> Result<S::Ok, S::Error> where S: Serializer {
        unimplemented!("custom serialization")
    }
    pub fn deserialize<'de, D>(d: D) -> Result<MyFields, D::Error> where D: Deserializer<'de> {
        unimplemented!("custom deserialization")
    }
}

#[derive(Serialize, Deserialize)]
enum Data {
    #[serde(with = "custom_module")]
    VariantName,
}

```

--------------------------------

### Serialize Some to JSON Value (Rust)

Source: https://serde.rs/impl-serializer

Illustrates the serialization of a present optional value (Some) into its contained JSON representation. Note that this is a lossy representation, as both Some(()) and None serialize to 'null'.

```Rust
    // A present optional is represented as just the contained value. Note that
    // this is a lossy representation. For example the values `Some(())` and
    // `None` both serialize as just `null`. Unfortunately this is typically
    // what people expect when working with JSON. Other formats are encouraged
    // to behave more intelligently if possible.
    fn serialize_some<T>(self, value: &T) -> Result<()>
    where
        T: ?Sized + Serialize,
    {
        value.serialize(self)
    }
```

--------------------------------

### Direct Deserialize Invocation with Serde

Source: https://serde.rs/remote-derive

Illustrates how to directly call the `deserialize` method generated by Serde's remote derive. This method takes a `Deserializer` as input and returns the deserialized type. Requires a `Deserializer` implementation.

```Rust
let mut de = serde_json::Deserializer::from_str(j);
let dur = DurationDef::deserialize(&mut de)?;

```

--------------------------------

### Serialize None to JSON Null (Rust)

Source: https://serde.rs/impl-serializer

Demonstrates how to serialize an absent optional value (None) into JSON null using Serde. This is part of the core serialization logic for optional types.

```Rust
    // An absent optional is represented as the JSON `null`.
    fn serialize_none(self) -> Result<()> {
        self.serialize_unit()
    }
```

--------------------------------

### Rust Serde: Basic Attribute Usage for Structs and Enums

Source: https://serde.rs/attributes

Demonstrates the application of Serde's container, variant, and field attributes to customize serialization and deserialization behavior for Rust structs and enums. It showcases how to deny unknown fields, set default values, and rename elements during the serialization process. These attributes require Rust 1.15 or newer.

```Rust
#[derive(Serialize, Deserialize)]
#[serde(deny_unknown_fields)]  // <-- this is a container attribute
struct S {
    #[serde(default)]  // <-- this is a field attribute
    f: i32,
}

#[derive(Serialize, Deserialize)]
#[serde(rename = "e")]  // <-- this is also a container attribute
enum E {
    #[serde(rename = "a")]  // <-- this is a variant attribute
    A(String),
}

```

--------------------------------

### Deserialize Struct with Serde RS

Source: https://serde.rs/impl-deserializer

Demonstrates deserializing a struct with integer and string vector fields from a JSON string using Serde RS. Requires the `Deserialize` derive macro and `from_str` function.

```rust
#[derive(Deserialize, PartialEq, Debug)]
struct Test {
    int: u32,
    seq: Vec<String>,
}

let j = r#"{"int":1,"seq":["a","b"]}"#;
let expected = Test {
    int: 1,
    seq: vec!["a".to_owned(), "b".to_owned()],
};
assert_eq!(expected, from_str(j).unwrap());
```

--------------------------------

### Rust: Independent Rename All for Serialization and Deserialization

Source: https://serde.rs/variant-attrs

Shows `#[serde(rename_all(serialize = "..."))]` and `#[serde(rename_all(deserialize = "..."))]` for different case conventions during serialization and deserialization.

```rust
#[derive(Serialize, Deserialize)]
#[serde(rename_all(serialize = "camelCase", deserialize = "snake_case"))]
enum Data {
    VariantName,
}

```

--------------------------------

### Rust: CommaSeparated for MapAccess

Source: https://serde.rs/impl-deserializer

Implements `MapAccess` for comma-separated map entries. It handles the comma before entries and the colon separating keys and values.

```rust
impl<'de, 'a> MapAccess<'de> for CommaSeparated<'a, 'de> {
    type Error = Error;

    fn next_key_seed<K>(&mut self, seed: K) -> Result<Option<K::Value>>
    where
        K: DeserializeSeed<'de>,
    {
        // Check if there are no more entries.
        if self.de.peek_char()? == '}' {
            return Ok(None);
        }
        // Comma is required before every entry except the first.
        if !self.first && self.de.next_char()? != ',' {
            return Err(Error::ExpectedMapComma);
        }
        self.first = false;
        // Deserialize a map key.
        seed.deserialize(&mut *self.de).map(Some)
    }

    fn next_value_seed<V>(&mut self, seed: V) -> Result<V::Value>
    where
        V: DeserializeSeed<'de>,
    {
        // It doesn't make a difference whether the colon is parsed at the end
        // of `next_key_seed` or at the beginning of `next_value_seed`. In this
        // case the code is a bit simpler having it here.
        if self.de.next_char()? != ':' {
            return Err(Error::ExpectedMapColon);
        }
        // Deserialize a map value.
        seed.deserialize(&mut *self.de)
    }
}
```

--------------------------------

### Add serde_repr Dependency

Source: https://serde.rs/enum-number

This snippet shows how to add the necessary serde_repr crate dependency to your Cargo.toml file. Ensure you have serde and serde_json also declared.

```toml
[dependencies]
serde = "1.0"
serde_json = "1.0"
serde_repr = "0.1"

```

--------------------------------

### Serde Struct Flattening: Capture additional fields with HashMap

Source: https://serde.rs/attr-flatten

Illustrates using `#[serde(flatten)]` with a `HashMap<String, Value>` to capture any fields not explicitly defined in the struct. This is valuable for handling extensible or partially known JSON structures.

```rust
use std::collections::HashMap;
use serde::{Serialize, Deserialize};
use serde_json::Value;

#[derive(Serialize, Deserialize)]
struct User {
    id: String,
    username: String,

    #[serde(flatten)]
    extra: HashMap<String, Value>,
}

```

--------------------------------

### Rust: Basic Rename Variant Attribute

Source: https://serde.rs/variant-attrs

Demonstrates how to use `#[serde(rename = "name")]` to specify a custom name for a variant during serialization and deserialization.

```rust
#[derive(Serialize, Deserialize)]
enum Data {
    #[serde(rename = "value")]
    VariantName,
}

```

--------------------------------

### Rust: Serialize Sequence with Serde

Source: https://serde.rs/impl-serializer

Implements Serde's `SerializeSeq` trait for a `Serializer`. This allows sequences to be serialized element by element, adding commas between elements and enclosing the entire sequence in square brackets `[]` in the JSON output. It handles the serialization of individual elements and the finalization of the sequence.

```rust
// This impl is SerializeSeq so these methods are called after `serialize_seq`
// is called on the Serializer.
implement<'a> ser::SerializeSeq for &'a mut Serializer {
    // Must match the `Ok` type of the serializer.
    type Ok = ();
    // Must match the `Error` type of the serializer.
    type Error = Error;

    // Serialize a single element of the sequence.
    fn serialize_element<T>(&mut self, value: &T) -> Result<()> 
    where
        T: ?Sized + Serialize,
    {
        if !self.output.ends_with('[') {
            self.output += ",";
        }
        value.serialize(&mut **self)
    }

    // Close the sequence.
    fn end(self) -> Result<()> {
        self.output += "]";
        Ok(())
    }
}
```