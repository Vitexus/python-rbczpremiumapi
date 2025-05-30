<?php

/**
 * GetBatchDetail200ResponseBatchItemsInnerAccountInfo
 *
 * PHP version 7.4
 *
 * @category Class
 * @package  rbczpremiumapi
 * @author   OpenAPI Generator team
 * @link     https://openapi-generator.tech
 */

/**
 * Production
 *
 * ##### API Overview - Accounts list and balance - Transaction overview (also for saving accounts) - Payments import - Statement list and download - FX rates  ##### Authentication Before making a call to Premium API, you need to register your app at our _Developer portal_. This is where you get the **ClientID** that your application must send in the request as `X-IBM-Client-Id`. This is the key that grants your app access to the API.  However, this may not be enough. Your application needs to use mTLS to call most operations here. Thus, you not only need _https_ but also a client certificate issued by us. The exception is two operations for FX rates that are accessible also without a client certificate.  Each bank client/user can issue several certificates. Each certificate can permit different sets of operations (http methods) on different bank accounts. All this must be configured in Internet Banking first by each bank client/user (bank clients need to look under _Settings_ and do not forget to download the certificate at the last step). The certificate is downloaded in **PKCS#12** format as **\\*.p12** file and protected by a password chosen by the bank client/user. Yes, your app needs the password as well to get use of the **\\*p12** file for establishing mTLS connection to the bank.  Client certificates issued in Internet Banking for bank clients/users have limited validity (e.g. **5 years**). However, **each year** certificates are automatically blocked and bank client/user must unblock them in Internet Banking. It is possible to do it in advance and prolong the time before the certificate is blocked. Your app should be prepared for these scenarios and it should communicate such cases to your user in advance to provide seamless service and high user-experience of your app.  ##### Rate Limiting The number of requests in each API operation is limited to 10 per client per sliding second and 5000 per client per sliding day. The exception is the 'Download Statement' operation with the limits lowered to 5 per client per sliding second and 1500 per client per sliding day. This is because it transports potentially sizeable binary files. The consumer must be able to handle HTTP status 429 in case of exceeding these limits.  Response headers `X-RateLimit-Limit-Second` and `X-RateLimit-Limit-Day` show the actual limits configured for the specific operation. Response headers `X-RateLimit-Remaining-Second` and `X-RateLimit-Remaining-Day` are returned to help prevent the limits from being exceeded.  ##### Notes Be aware, that in certain error situations, API can return specific error structures along with 5xx status code, which is not explicitely defined below.  ##### Quick Start Client Feel free to download a <a href=\"assets/PremiumApiClient.java\" download>simple Java client</a> that gives you quick access to our API. 
 *
 * The version of the OpenAPI document: 1.1.20240910
 * Contact: info@vitexsoftware.cz
 * Generated by: https://openapi-generator.tech
 * Generator version: 7.13.0
 */

/**
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

namespace rbczpremiumapi.Model;

use \ArrayAccess;
use \rbczpremiumapi\ObjectSerializer;

/**
 * GetBatchDetail200ResponseBatchItemsInnerAccountInfo Class Doc Comment
 *
 * @category Class
 * @description Account info detail
 * @package  rbczpremiumapi
 * @author   OpenAPI Generator team
 * @link     https://openapi-generator.tech
 * @implements \ArrayAccess<string, mixed>
 */
class GetBatchDetail200ResponseBatchItemsInnerAccountInfo implements ModelInterface, ArrayAccess, \JsonSerializable
{
    public const DISCRIMINATOR = null;

    /**
      * The original name of the model.
      *
      * @var string
      */
    protected static $openAPIModelName = 'getBatchDetail_200_response_batchItems_inner_accountInfo';

    /**
      * Array of property to type mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $openAPITypes = [
        'account_id' => 'int',
        'account_number_prefix' => 'str',
        'account_number' => 'str',
        'main_currency_id' => 'str'
    ];

    /**
      * Array of property to format mappings. Used for (de)serialization
      *
      * @var string[]
      * @phpstan-var array<string, string|null>
      * @psalm-var array<string, string|null>
      */
    protected static $openAPIFormats = [
        'account_id' => 'int64',
        'account_number_prefix' => null,
        'account_number' => null,
        'main_currency_id' => null
    ];

    /**
      * Array of nullable properties. Used for (de)serialization
      *
      * @var boolean[]
      */
    protected static array $openAPINullables = [
        'account_id' => false,
        'account_number_prefix' => false,
        'account_number' => false,
        'main_currency_id' => false
    ];

    /**
      * If a nullable field gets set to null, insert it here
      *
      * @var boolean[]
      */
    protected array $openAPINullablesSetToNull = [];

    /**
     * Array of property to type mappings. Used for (de)serialization
     *
     * @return array
     */
    public static function openAPITypes()
    {
        return self::$openAPITypes;
    }

    /**
     * Array of property to format mappings. Used for (de)serialization
     *
     * @return array
     */
    public static function openAPIFormats()
    {
        return self::$openAPIFormats;
    }

    /**
     * Array of nullable properties
     *
     * @return array
     */
    protected static function openAPINullables(): array
    {
        return self::$openAPINullables;
    }

    /**
     * Array of nullable field names deliberately set to null
     *
     * @return boolean[]
     */
    private function getOpenAPINullablesSetToNull(): array
    {
        return $this->openAPINullablesSetToNull;
    }

    /**
     * Setter - Array of nullable field names deliberately set to null
     *
     * @param boolean[] $openAPINullablesSetToNull
     */
    private function setOpenAPINullablesSetToNull(array $openAPINullablesSetToNull): void
    {
        $this->openAPINullablesSetToNull = $openAPINullablesSetToNull;
    }

    /**
     * Checks if a property is nullable
     *
     * @param string $property
     * @return bool
     */
    public static function isNullable(string $property): bool
    {
        return self::openAPINullables()[$property] ?? false;
    }

    /**
     * Checks if a nullable property is set to null.
     *
     * @param string $property
     * @return bool
     */
    public function isNullableSetToNull(string $property): bool
    {
        return in_array($property, $this->getOpenAPINullablesSetToNull(), true);
    }

    /**
     * Array of attributes where the key is the local name,
     * and the value is the original name
     *
     * @var string[]
     */
    protected static $attributeMap = [
        'account_id' => 'accountId',
        'account_number_prefix' => 'accountNumberPrefix',
        'account_number' => 'accountNumber',
        'main_currency_id' => 'mainCurrencyId'
    ];

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @var string[]
     */
    protected static $setters = [
        'account_id' => 'setAccountId',
        'account_number_prefix' => 'setAccountNumberPrefix',
        'account_number' => 'setAccountNumber',
        'main_currency_id' => 'setMainCurrencyId'
    ];

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @var string[]
     */
    protected static $getters = [
        'account_id' => 'getAccountId',
        'account_number_prefix' => 'getAccountNumberPrefix',
        'account_number' => 'getAccountNumber',
        'main_currency_id' => 'getMainCurrencyId'
    ];

    /**
     * Array of attributes where the key is the local name,
     * and the value is the original name
     *
     * @return array
     */
    public static function attributeMap()
    {
        return self::$attributeMap;
    }

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @return array
     */
    public static function setters()
    {
        return self::$setters;
    }

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @return array
     */
    public static function getters()
    {
        return self::$getters;
    }

    /**
     * The original name of the model.
     *
     * @return string
     */
    public function getModelName()
    {
        return self::$openAPIModelName;
    }


    /**
     * Associative array for storing property values
     *
     * @var mixed[]
     */
    protected $container = [];

    /**
     * Constructor
     *
     * @param mixed[]|null $data Associated array of property values
     *                      initializing the model
     */
    public function __construct(?array $data = null)
    {
        $this->setIfExists('account_id', $data ?? [], null);
        $this->setIfExists('account_number_prefix', $data ?? [], null);
        $this->setIfExists('account_number', $data ?? [], null);
        $this->setIfExists('main_currency_id', $data ?? [], null);
    }

    /**
    * Sets $this->container[$variableName] to the given data or to the given default Value; if $variableName
    * is nullable and its value is set to null in the $fields array, then mark it as "set to null" in the
    * $this->openAPINullablesSetToNull array
    *
    * @param string $variableName
    * @param array  $fields
    * @param mixed  $defaultValue
    */
    private function setIfExists(string $variableName, array $fields, $defaultValue): void
    {
        if (self::isNullable($variableName) && array_key_exists($variableName, $fields) && is_null($fields[$variableName])) {
            $this->openAPINullablesSetToNull[] = $variableName;
        }

        $this->container[$variableName] = $fields[$variableName] ?? $defaultValue;
    }

    /**
     * Show all the invalid properties with reasons.
     *
     * @return array invalid properties with reasons
     */
    public function listInvalidProperties()
    {
        $invalidProperties = [];

        if ($this->container['account_id'] === null) {
            $invalidProperties[] = "'account_id' can't be null";
        }
        if ($this->container['account_number'] === null) {
            $invalidProperties[] = "'account_number' can't be null";
        }
        if ($this->container['main_currency_id'] === null) {
            $invalidProperties[] = "'main_currency_id' can't be null";
        }
        if ((mb_strlen((string)$this->container['main_currency_id']) > 3)) {
            $invalidProperties[] = "invalid value for 'main_currency_id', the character length must be smaller than or equal to 3.";
        }

        if ((mb_strlen((string)$this->container['main_currency_id']) < 3)) {
            $invalidProperties[] = "invalid value for 'main_currency_id', the character length must be bigger than or equal to 3.";
        }

        return $invalidProperties;
    }

    /**
     * Validate all the properties in the model
     * return true if all passed
     *
     * @return bool True if all properties are valid
     */
    public function valid()
    {
        return count($this->listInvalidProperties()) === 0;
    }


    /**
     * Gets account_id
     *
     * @return int
     */
    public function getAccountId()
    {
        return $this->container['account_id'];
    }

    /**
     * Sets account_id
     *
     * @param int $account_id Account Id.
     *
     * @return self
     */
    public function setAccountId($account_id)
    {
        if (is_null($account_id)) {
            throw new \InvalidArgumentException('non-nullable account_id cannot be null');
        }
        $this->container['account_id'] = $account_id;

        return $this;
    }

    /**
     * Gets account_number_prefix
     *
     * @return str|null
     */
    public function getAccountNumberPrefix()
    {
        return $this->container['account_number_prefix'];
    }

    /**
     * Sets account_number_prefix
     *
     * @param str|null $account_number_prefix Charged account number prefix
     *
     * @return self
     */
    public function setAccountNumberPrefix($account_number_prefix)
    {
        if (is_null($account_number_prefix)) {
            throw new \InvalidArgumentException('non-nullable account_number_prefix cannot be null');
        }
        $this->container['account_number_prefix'] = $account_number_prefix;

        return $this;
    }

    /**
     * Gets account_number
     *
     * @return str
     */
    public function getAccountNumber()
    {
        return $this->container['account_number'];
    }

    /**
     * Sets account_number
     *
     * @param str $account_number Charged account number
     *
     * @return self
     */
    public function setAccountNumber($account_number)
    {
        if (is_null($account_number)) {
            throw new \InvalidArgumentException('non-nullable account_number cannot be null');
        }
        $this->container['account_number'] = $account_number;

        return $this;
    }

    /**
     * Gets main_currency_id
     *
     * @return str
     */
    public function getMainCurrencyId()
    {
        return $this->container['main_currency_id'];
    }

    /**
     * Sets main_currency_id
     *
     * @param str $main_currency_id The currency folder identification (CATALOG: CURRENCIES)
     *
     * @return self
     */
    public function setMainCurrencyId($main_currency_id)
    {
        if (is_null($main_currency_id)) {
            throw new \InvalidArgumentException('non-nullable main_currency_id cannot be null');
        }
        if ((mb_strlen((string)$main_currency_id) > 3)) {
            throw new \InvalidArgumentException('invalid length for $main_currency_id when calling GetBatchDetail200ResponseBatchItemsInnerAccountInfo., must be smaller than or equal to 3.');
        }
        if ((mb_strlen((string)$main_currency_id) < 3)) {
            throw new \InvalidArgumentException('invalid length for $main_currency_id when calling GetBatchDetail200ResponseBatchItemsInnerAccountInfo., must be bigger than or equal to 3.');
        }

        $this->container['main_currency_id'] = $main_currency_id;

        return $this;
    }
    /**
     * Returns true if offset exists. False otherwise.
     *
     * @param integer $offset Offset
     *
     * @return boolean
     */
    public function offsetExists($offset): bool
    {
        return isset($this->container[$offset]);
    }

    /**
     * Gets offset.
     *
     * @param integer $offset Offset
     *
     * @return mixed|null
     */
    #[\ReturnTypeWillChange]
    public function offsetGet($offset)
    {
        return $this->container[$offset] ?? null;
    }

    /**
     * Sets value based on offset.
     *
     * @param int|null $offset Offset
     * @param mixed    $value  Value to be set
     *
     * @return void
     */
    public function offsetSet($offset, $value): void
    {
        if (is_null($offset)) {
            $this->container[] = $value;
        } else {
            $this->container[$offset] = $value;
        }
    }

    /**
     * Unsets offset.
     *
     * @param integer $offset Offset
     *
     * @return void
     */
    public function offsetUnset($offset): void
    {
        unset($this->container[$offset]);
    }

    /**
     * Serializes the object to a value that can be serialized natively by json_encode().
     * @link https://www.php.net/manual/en/jsonserializable.jsonserialize.php
     *
     * @return mixed Returns data which can be serialized by json_encode(), which is a value
     * of any type other than a resource.
     */
    #[\ReturnTypeWillChange]
    public function jsonSerialize()
    {
        return ObjectSerializer::sanitizeForSerialization($this);
    }

    /**
     * Gets the string presentation of the object
     *
     * @return string
     */
    public function __toString()
    {
        return json_encode(
            ObjectSerializer::sanitizeForSerialization($this),
            JSON_PRETTY_PRINT
        );
    }

    /**
     * Gets a header-safe presentation of the object
     *
     * @return string
     */
    public function toHeaderValue()
    {
        return json_encode(ObjectSerializer::sanitizeForSerialization($this));
    }
}


